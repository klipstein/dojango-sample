from dojango.data.modelstore.treestore import TreeStore
from dojango.data.modelstore.fields import StoreField

from models import Post

class MPTreeStore(TreeStore):
    
    name  = StoreField(model_field="author")
    comment = StoreField()
    
    class Meta:
        objects = Post.objects.filter(id__in=(1,2,))
        label = 'name'
