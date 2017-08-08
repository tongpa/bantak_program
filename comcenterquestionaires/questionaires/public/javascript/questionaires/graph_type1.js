Ext.require('Ext.chart.*');
Ext.require(['Ext.Window', 'Ext.fx.target.Sprite', 'Ext.layout.container.Fit', 'Ext.window.MessageBox']);

Ext.chart.theme.myTheme = Ext.extend(Ext.chart.theme.Base,{
	contructor : function(config){
		Ext.chart.theme.base.prototype.constructor.call(this, Ext.apply({
			colors : [
			          'rgb(0,255,128)',
			          'rgb(255,125,0)'
			          ]
			
		} ,config));
	}
	
});
Ext.onReady(function () {

	var store = Ext.create('Ext.data.JsonStore',{
		fields : ['name','old','new'],
		data : [
		        {'name' : '1', 'old' : 43, 'new' : 0},
		        {'name' : '2', 'old' : 23, 'new' : 23},
		        {'name' : '3', 'old' : 25, 'new' : 43},
		        {'name' : '4', 'old' : 0, 'new' : 4},
		        {'name' : '5', 'old' : 0, 'new' : 2} 
		        
		        ]
		
	});
	
	Ext.regModel('chartcompair', {
	    fields: [
	    	{name: 'name' }  ,
	         {name: 'old' }  ,
	         {name: 'new' }  
	    ]
	});
	
	var storeCompair =   new Ext.data.Store({
		model : 'chartcompair',
		proxy: {
	        type: 'ajax',
	        url : '/quest/queryBySumLevelBy',
	        reader: {
	            type: 'json',
	            root: 'root'
	        }
	    },
	    autoLoad: true
	});

	//storeCompair.load();
	 
	var chart = Ext.create('Ext.chart.Chart', {
			
            id: 'chartCmp',
            xtype: 'chart',
            style: 'background:#fff',
            animate: true,
            shadow: true,
            store: storeCompair,
            legend: {
              position: 'right'  
            },
            axes: [{
            	
                type: 'Numeric',
                position: 'left', 
                fields: ['old', 'new'],
                minimum: 0,
                label: {
                    renderer: Ext.util.Format.numberRenderer('0,0')
                },
                grid: true,
                title: 'จำนวน'
            }, {
                type: 'Category',
               
                position: 'bottom',
                fields: ['name'],
                title: 'ระดับความพึงพอใจ'
            }],
            series: [{
            	title: 'test',
            	showInLegend : true,
                type: 'column',
              
                axis : 'left',
                yField: ['old', 'new'],
                title : ['ระบบเก่า','ระบบใหม่'],
                xField:  'name'	,
              //  stacked : true,
                tips : {
                	trackMouse : true,
                	width : 25,
                	height : 28,
                	renderer : function (storeItem ,item){
                		this.setTitle(String(item.value[1]));
                	}
                },
                getLegendColor: function(index){
                	return ['#add8e6', '#f08080' ][index%2];
                }
                ,
                renderer:function(sprite,record,attr,index,store){
                	return Ext.apply(attr,{
                		fill: ['#add8e6', '#f08080' ][index%2]
                	});
                },
                highlight: true,
                label: {
                  display: 'insideEnd',
                  'text-anchor': 'middle',
                    field:  ['old', 'new'],
                    orientation: 'horizontal',
                     
                    fill: '#AA',
                    font: '14px Arial'
                }
            }]
        });


    var win = Ext.create('Ext.Window', {
        width: 800,
        height: 600,
        minHeight: 400,
        minWidth: 550,
        hidden: false,
        maximizable: true,
        title: 'Grouped Bar Chart',
        renderTo: Ext.getBody(),
        layout: 'fit',
        tbar: [{
            text: 'Save Chart',
            handler: function() {
                Ext.MessageBox.confirm('Confirm Download', 'Would you like to download the chart as an image?', function(choice){
                    if(choice == 'yes'){
                        chart.save({
                            type: 'image/png'
                        });
                    }
                });
            }
        }, {
            text: 'Reload Data',
            handler: function() {
                store1.loadData(generateData());
            }
        }, {
            enableToggle: true,
            pressed: true,
            text: 'Animate',
            toggleHandler: function(btn, pressed) {
                var chart = Ext.getCmp('chartCmp');
                chart.animate = pressed ? { easing: 'ease', duration: 500 } : false;
            }
        }],
        items: chart
    });
});
