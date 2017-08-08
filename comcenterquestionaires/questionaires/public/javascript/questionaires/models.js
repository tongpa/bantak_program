Ext.namespace("question");

Ext.regModel('chartcompair', {
    fields: [
    	{name: 'name' }  ,
         {name: 'old' }  ,
         {name: 'new' }  ,
         {name: 'pnew', type: 'float' }  ,
         {name: 'pold', type: 'float' }  
    ]
});


Ext.regModel('chartavg', {
    fields: [
    	 {name: 'name' }  ,
         {name: 'm_old' }   ,
         {name: 'm_new' }   
    ]
});

Ext.regModel('chartgroup', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' }  ,
         {name: 'm_old' }   ,
         {name: 'm_new' }   ,
         {name: 'std_old' }   ,
         {name: 'std_new' }  
    ]
});


question.storeGroup1 =   new Ext.data.Store({
	model : 'chartgroup',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByMedianGroup?group=1',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: true
});



question.storeCompair =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=ao1&column2=an1',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

question.storeCompair2 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=ao2&column2=an2',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

question.storeCompair3 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=ao3&column2=an3',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
question.storeCompair4 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=ao4&column2=an4',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
question.storeCompair5 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=ao5&column2=an5',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
question.storeCompair6 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=ao6&column2=an6',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 


question.storeCompair7 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=bo1&column2=bn1',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompair8 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=bo2&column2=bn2',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompair9 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=bo3&column2=bn3',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 
question.storeCompair10 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=bo4&column2=bn4',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 


question.storeCompair11 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=bo5&column2=bn5',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompair12 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=bo6&column2=bn6',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompair13 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=bo7&column2=bn7',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompair14 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=co1&column2=cn1',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 
question.storeCompair15 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=co2&column2=cn2',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 
question.storeCompair16 =   new Ext.data.Store({
	model : 'chartcompair',
	proxy: {
        type: 'ajax',
        url : '/quest/queryBySumLevelBy?column1=co3&column2=cn3',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

////////////////////////////////////////////////////////////////////////////////
 
question.storeCompairAvg =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=ao1&column2=an1',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});


question.storeCompairAvg2 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=ao2&column2=an2',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});


question.storeCompairAvg3 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=ao3&column2=an3',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
question.storeCompairAvg4 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=ao4&column2=an4',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
question.storeCompairAvg5 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=ao5&column2=an5',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
question.storeCompairAvg6 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=ao6&column2=an6',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 


question.storeCompairAvg7 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=bo1&column2=bn1',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompairAvg8 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=bo2&column2=bn2',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompairAvg9 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=bo3&column2=bn3',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 
question.storeCompairAvg10 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=bo4&column2=bn4',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 


question.storeCompairAvg11 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=bo5&column2=bn5',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompairAvg12 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=bo6&column2=bn6',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompairAvg13 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=bo7&column2=bn7',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

question.storeCompairAvg14 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=co1&column2=cn1',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 
question.storeCompairAvg15 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=co2&column2=cn2',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 
question.storeCompairAvg16 =   new Ext.data.Store({
	model : 'chartavg',
	proxy: {
        type: 'ajax',
        url : '/quest/queryByAvgBy?column1=co3&column2=cn3',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

