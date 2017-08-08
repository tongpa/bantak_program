Ext.namespace("coms");

Ext.regModel('namevalue', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' }  
    ]
});

Ext.regModel('responsevalue', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' }  ,
         {name: 'detail'}
    ]
});


coms.listComputerTypes =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/computer/listComputerTypes',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

