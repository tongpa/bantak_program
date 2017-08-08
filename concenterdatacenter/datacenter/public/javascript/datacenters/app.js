
Ext.require([
    'Ext.tip.QuickTipManager',
    'Ext.container.Viewport',
    'Ext.layout.*',
    'Ext.form.Panel',
    'Ext.form.Label',
    'Ext.grid.*',
    'Ext.data.*',
    'Ext.tree.*',
    'Ext.selection.*',
    'Ext.tab.Panel'  
]);

Ext.application({
    name: 'datacenter',
    launch: function() {
    
    	var layoutExamples = [panel1];
    	
    	
    	var panel1 = Ext.create('Ext.form.Panel',{
    		title   : 'รายละเอียด',
    		id : '1-panel',
    		itemId: 'card-0',
            autoHeight: true,
            width   : '100%',
             
            defaults: {
                anchor: '100%',
                labelWidth: 100
            }
    	});
    	
    	var panel2 = Ext.create('Ext.form.Panel',{
    		title   : 'FieldContainers2',
    		id : '2-panel',
            autoHeight: true,
            width   : '100%',
            itemId: 'card-1', 
            defaults: {
                anchor: '100%',
                labelWidth: 100
            }
    	});
    	
 
    	
    	var contentPanel =   Ext.create('Ext.panel.Panel', { 
    	         id: 'content-panel',
    	         region: 'center', // this is what makes this panel into a region within the containing layout
    	         layout: 'card',
    	        // title: 'Menu',
    	       //  margins: '2 5 5 0',
    	         activeItem: 0,
    	         border: false,
    	         collapsible: false,
    	         items: [panel1,panel2]
    	    });
    	
    	
    	 
    	
    	var treePanel = Ext.create('Ext.tree.Panel', {
            id: 'tree-panel',
            title: 'Menu',
            region:'north',
            split: true,
            region:'west',
    	    margins: '5 0 0 0',
    	    cmargins: '5 5 0 0',
    	    width: 250,
    	    minSize: 150,
    	    maxSize: 250,
    	    
            autoHeight: true,
            collapsible: true, 
            rootVisible: false,
            autoScroll: true,
            store:  datacenter.menuTreeStore
        }); 
    	
    	// Assign the changeLayout function to be called on tree node click.
        treePanel.getSelectionModel().on('select', function(selModel, record) {
        	console.log('select');
            if (record.get('leaf')) {
            	//console.log('select content-panel :' + record.getId());
                
            	//contentPanel.getLayout().setActiveItem(2);
            	//panel.getLayout().setActiveItem(card2);
            	var l = Ext.getCmp('content-panel').getLayout();
            	//var i = l.activeItem.id.split('card-')[1];
            	 //var next = parseInt(i, 10) + 1;
            	
            	//comment used
            	//l.setActiveItem(parseInt(record.getId(),10) -1);
            	l.getActiveItem().setTitle(record.data.text);
            	 
            }
        });
    	
    	
        var panel = new Ext.form.Panel({
        	layout:'border',
        	height : 800,
        	renderTo : 'maintenance-app',
        	defaults: {
        	    collapsible: true,
        	    split: true 
        	   // bodyStyle: 'padding:15px'
        	} 
        	,
        	items: [ treePanel,contentPanel]
        });
    	//debugger;
    	 
    }
});
Ext.namespace("datacenter"); 


function getCustomLayouts() {
    return {
        /*
         * CenterLayout demo panel
         */
        centerLayout: {
            id: 'center-panel',
            layout: 'ux.center',
            items: {
                title: 'Centered Panel: 75% of container width and 95% height',
                layout: 'ux.center',
                autoScroll: true,
                width: '75%',
                height: '95%',
                bodyStyle: 'padding:20px 0;',
                items: [{
                    title: 'Inner Centered Panel',
                    html: 'Fixed 300px wide and full height. The container panel will also autoscroll if narrower than 300px.',
                    width: 300,
                    frame: true,
                    bodyStyle: 'padding:10px 20px;'
                }]
            }
        }
    };

}
 