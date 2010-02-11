dependencies = {
        layers: [
                {
                        name: "../moviedb/show.js",
                        layerDependencies: [
                        ],
                        dependencies: [
                                "moviedb.show"
                        ]
                }
        ],

        prefixes: [
                [ "dijit", "../dijit" ],
                [ "dojox", "../dojox" ],
                [ "dojango", "../../../../external_apps/dojango/dojo-media/dojango" ],
                [ "moviedb", "../../../../core/dojo-media/moviedb"]
        ]
}
