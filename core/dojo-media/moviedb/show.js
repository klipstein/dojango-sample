dojo.provide("moviedb.show");

dojo.require("dojo.parser");
dojo.require("dijit.layout.BorderContainer");
dojo.require("dijit.layout.ContentPane");
dojo.require("dojox.layout.ContentPane");
dojo.require("dojox.grid.DataGrid");
//dojo.require("dojox.data.ClientFilter");
dojo.require("dojox.data.JsonRestStore");

// used for cropping the biography of an actor
dojo.require("dojox.dtl.filter.strings")

dojo.ready(function(){
	moviedb.show.movieStore = new dojox.data.JsonRestStore({
		target:"/api/movies",
		syncMode:true
	});
	var grid = dijit.byId("movieGrid");
	grid.setStore(moviedb.show.movieStore);
	grid.connect(grid, "onRowClick", function(el){
		var item = this.getItem(el.rowIndex);
		moviedb.show.showDetails(item);
	});
	window.setTimeout(function(){ // would require a separate parse process!
		dijit.byId("mainBC").resize();
	}, 100);
});

dojo.mixin(moviedb.show, {
	
	movieStore: null,
	
	showImage: function (item){
		return '<img style="height:100px;" src="/static/' + item + '"/>';
	},

	prevContainer: null,
	showDetails: function (item){
		var bc = dijit.byId("mainBC");
		this.prevContainer = dijit.byId("centerPane") ? dijit.byId("centerPane") : this.prevContainer;
		var detailBC = new dijit.layout.BorderContainer({
			region:"center"
		});
		var detailBCTop = new dijit.layout.BorderContainer({
			region: "top",
			splitter: true,
			style: "height:50%;"
		});
		var detailHeaderCP = new dijit.layout.ContentPane({
			region: "top",
			style: "height:27px;background:#AABFDC;",
			content: "<h1 style='margin-top:5px;'>Movie Details</h1>"
		});
		var detailCP = new dojox.layout.ContentPane({
			region: "center",
			href: "/show/" + item.id + "/",
			cleanContent:true,
			renderStyles:true,
			parseOnLoad:false
		});
		detailBCTop.addChild(detailHeaderCP);
		detailBCTop.addChild(detailCP);

		var store = new dojox.data.JsonRestStore({
			target: "/api/movies/" + item.id + "/actors/"
		});
		var actorsGrid = new dojox.grid.DataGrid({
			region: "center",
			store:store,
			structure: [
				{ field: "image", name: "Picture", width: "100px", formatter: this.showImage},
				{ field: "forename", name: "First name", width: "auto" },
				{ field: "surname", name: "Last name", width:"auto"},
				{ field: "biography", name: "biography", width:"auto", formatter: function(txt){
					return dojox.dtl.filter.strings.truncatewords(txt, 30) + (dojox.dtl.filter.strings.wordcount(txt) > 30 ? "..." : "");
				}}
			],
			queryOptions: {
				cache:true
			}
		});
		detailBC.addChild(detailBCTop);
		detailBC.addChild(actorsGrid);
		bc.removeChild(this.prevContainer);
		this.prevContainer.destroyDescendants();
		this.prevContainer.destroy();
		bc.addChild(detailBC);
		this.prevContainer = detailBC;
	}
});