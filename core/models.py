from django.db import models

# Create your models here.
from treebeard.mp_tree import MP_Node

class Post(MP_Node):
    author  = models.CharField(max_length=255)
    comment = models.TextField()
    #created = models.DateTimeField(auto_now_add=True)
    # Exception Value: Cannot use None as a query value
    created = models.DateTimeField(editable=False)

    node_order_by = ['created']

    def __unicode__(self):
        return u'Post %d: %s' % (self.id, self.comment)

    class Meta:
        verbose_name = 'Post (Materialized Path Tree)'
        # when adding a custom Meta class to a MP model, the ordering must be
        # set again
        ordering = ['path']

Post._meta.get_field('path').max_length = 255