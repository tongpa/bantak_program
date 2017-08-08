Ext.namespace("datacenter");

 
Ext.define('menubalue', {
    extend: 'Ext.data.Model',
    fields: [
        {name: 'id',    type: 'int'},
        {name: 'text',  type: 'string'} 
    ]
});
 
 

datacenter.menuTreeStore = Ext.create('Ext.data.TreeStore', {
	model : 'menubalue',
    root: {
        expanded: true
    },
    proxy: {
        type: 'ajax',
        url: '/datacenter/getMenu',
        reader: {
            type: 'json',
            root: 'children'
        }
    },
    autoLoad : true
});



Ext.define('User', {
    extend: 'Ext.data.Model',
    fields: [
        {name: 'id',    type: 'int'},
        {name: 'name',  type: 'string'},
        {name: 'phone', type: 'string', mapping: 'phoneNumber'}
    ]
});


//this data does not line up to our model fields - the phone field is called phoneNumber
var data = {
    users: [
        {
            id: 1,
            name: 'Ed Spencer',
            phoneNumber: '555 1234'
        },
        {
            id: 2,
            name: 'Abe Elias',
            phoneNumber: '666 1234'
        }
    ]
};
 