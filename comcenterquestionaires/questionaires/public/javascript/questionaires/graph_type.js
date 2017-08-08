Ext.require('Ext.chart.*');
Ext.require(['Ext.Window', 'Ext.fx.target.Sprite', 'Ext.layout.container.Fit', 'Ext.window.MessageBox','Ext.util']);

Ext.define('ChartGraph',{
	extend : 'Ext.form.Panel',
	fields_catelogy :['pold', 'pnew'],
	fields_name : 'name', 
	legend_title : ['ระบบอุบัติการณ์เดิม','ระบบอุบัติการณ์ออนไลน์'],
	 
	xtitle: 'ระดับความพึงพอใจ',
	ytitle: 'ร้อยละ',
	title_panel : '',
	fields_catelogy_avg : ['m_old','m_new'],
	fields_name_avg : 'name',
	xtitle_avg : 'ค่าเฉลี่ย',
	ytitle_avg : 'ระดับความพึงพอใจ', 
	color_show1 : '#FFFFFF' ,
	color_show2 : '#858484'  ,
	barwidth : 45,
	storeChart : question.storeCompair,
	storeTable : question.storeGroup1,
	storeChartAvg : question.storeCompairAvg,
    initComponent: function() {
    	var main = this;
    	
    	
    	main.table = Ext.create('Ext.grid.Panel',{
    		columnLines: true,
    		store : main.storeChart,
    		columns :  [
    		    {	text : 'ระดับความพึงพอใจ',
    		    	width : 100,
    		    	dataIndex : 'name',
    		    	flex : 1
    		    } ,
    		    {
    		    	text : 'ระบบเก่า',
    		    	columns : [
    		    	   {
    		    		   text : 'จำนวน',
    		    		   width : 75,
    		    		   dataIndex : 'old'
    		    	   } ,
    		    	   {
    		    		   text : 'ร้อยละ',
    		    		   width : 75,
    		    		   dataIndex : 'pold',
    		    		   renderer : function(value,record){
    		    			   var val = Ext.util.Format.number(value,'0.00');
    	                    	val =  val.replace(",",".");   
    		    			   return val;
    		    		   }
    		    	   }
    		    	]
    		    } ,
    		    {
    		    	text : 'ระบบใหม่',
    		    	columns : [
    		    	   {
    		    		   text : 'จำนวน',
    		    		   width : 75,
    		    		   dataIndex : 'new'
    		    	   } ,
    		    	   {
    		    		   text : 'ร้อยละ',
    		    		   width : 75,
    		    		   dataIndex : 'pnew',
    		    		   renderer : function(value,record){
    		    			   var val = Ext.util.Format.number(value,'0.00');
    	                    	val =  val.replace(",",".");   
    		    			   return val;
    		    		   }
    		    	   }
    		    	]
    		    }
    		            
    		 ] ,
    		 viewConfig :{
    			 stripeRows :true
    		 },
    	        height: 350,
    	        width: 600
    	});
    	
    	main.chart = Ext.create('Ext.chart.Chart', {
			
        //    id: 'chartCmp',
            xtype: 'chart',
            style: 'background:#fff',
            animate: true,
            shadow: true,
            store: main.storeChart,
            legend: {
              //position: 'right'  
            	position: 'top'  
            	//labelFont : '16px Angsana New'
            },
            axes: [{
            	
                type: 'Numeric',
                position: 'left', 
                fields: main.fields_catelogy ,//['old', 'new'],
                minimum: 0,
                label: {
                    renderer: Ext.util.Format.numberRenderer('0,0')
                },
                grid: true,
                title: main.ytitle //'จำนวน'
            }, {
                type: 'Category',               
                position: 'bottom',
                fields: main.fields_name ,// ['name'],
                title: main.xtitle //'ระดับความพึงพอใจ'
            }],
            series: [{
            	title: 'test',
            	showInLegend : true,
                type: 'column',
                style: {width:45},
                axis : 'left',
                yField:  main.fields_catelogy ,//['old', 'new'],
                title : main.legend_title,// ['ระบบเก่า','ระบบใหม่'],
                xField:  main.fields_name ,// 	,
              //  stacked : true,
                tips : {
                	trackMouse : true,
                	width : 56,
                	height : 28,
                	renderer : function (storeItem ,item){
                		var val = Ext.util.Format.number(item.value[1],'0.00');
                		 
                    	val =  val.replace(",",".") + "%";   
                		this.setTitle(String(val  )  );
                	}
                },
                getLegendColor: function(index){
                	//return ['#add8e6', '#f08080' ][index%2];
                	// return ['#FFFFFF', '#858484' ][index%2];
                	 return [main.color_show1,main.color_show2][index%2];
                }
                ,
                renderer:function(sprite,record,attr,index,store){
                	
                	fill_color = Ext.apply(attr,{
                		//fill: ['#add8e6', '#f08080' ][index%2]
                		//fill: ['#FFFFFF', '#858484' ][index%2],
                		fill:[main.color_show1,main.color_show2][index%2],
                		"stroke-width": [4, 0 ][index%2] ,
                		stroke :  'black' 
                		
                	});
                	
                	return fill_color;
                	
                },
                highlight: true,
                label: {
                  display: 'insideEnd',
                  'text-anchor': 'middle',
                    field:  main.fields_catelogy ,// ['old', 'new'],
                    orientation: 'horizontal',
                     
                    fill: '#AA',
                    font: '14px Arial' ,
                    renderer: function(v){
                    	var val = Ext.util.Format.number(v,'0.00');
                    	val =  val.replace(",",".");                    	 
                    	return val;
                    }
                }
            }]
        });
    	
    	
    	main.chartAvg = Ext.create('Ext.chart.Chart', {
			
            //    id: 'chartCmp',
                xtype: 'chart',
                style: 'background:#fff',
                animate: true,
                shadow: true,
                store: main.storeChartAvg,
                legend: {
                  position: 'top'  
                },
                
                axes: [{
                	
                    type: 'Numeric',
                    position: 'left', 
                    fields:  main.fields_catelogy_avg  ,//['old', 'new'],
                    minimum: 0, 
                    maximum : 5,
                  
                    label: {
                    	//rotate : {degrees: 315},
                        renderer: Ext.util.Format.numberRenderer('0,0')
                    },
                    steps : 6,
                    grid: true,
                    title: main.ytitle_avg //'จำนวน'
                }, {
                    type: 'Category',               
                    position: 'bottom',
                    fields: main.fields_name_avg ,// ['name'],
                    title: main.xtitle_avg //'ระดับความพึงพอใจ'
                }],
                series: [{
                	
                	showInLegend : true,
                    type: 'column',
                    style:{width:45},
                    axis : 'left',
                    yField:   main.fields_catelogy_avg  ,//['old', 'new'],
                    title : main.legend_title,// ['ระบบเก่า','ระบบใหม่'],
                    xField:  main.fields_name_avg ,// 	,
                  //  stacked : true,
                    tips : {
                    	trackMouse : true,
                    	width : 56,
                    	height : 28,
                    	renderer : function (storeItem ,item){
                    		var val = Ext.util.Format.number(item.value[1],'0.00');
                    		 
                        	val =  val.replace(",",".")  ;   
                    		this.setTitle(String(val  )  );
                    	}
                    },
                    getLegendColor: function(index){
                    	//return ['#add8e6', '#f08080' ][index%2];
                    	return [main.color_show1,main.color_show2][index%2];
                    }
                    ,
                    renderer:function(sprite,record,attr,index,store){
                    	return Ext.apply(attr,{
                    		//fill: ['#add8e6', '#f08080' ][index%2]
                    		fill :[main.color_show1,main.color_show2][index%2]
                    		 
                    	});
                    },
                    highlight: true,
                    label: {
                      display: 'insideEnd',
                      'text-anchor': 'middle',
                        field:  main.fields_catelogy_avg ,// ['old', 'new'],
                        orientation: 'horizontal',
                         
                        fill: '#AA',
                        font: '14px Arial' ,
                        renderer: function(v){
                        	var val = Ext.util.Format.number(v,'0.00');
                        	val =  val.replace(",",".");                    	 
                        	return val;
                        }
                    }
                }]
            });
    	
    	main.panel1 = Ext.create('widget.panel', {
    		width: '100%',
    		//width: '500',
    		height: 400,
            title: main.title_panel,
             
            layout: 'fit',
           /* tbar: [{
                text: 'Save Chart' 
               // handler: function(){ downloadChart(chart1); }
            }],*/
            items: [main.chart]
        });
    	
    	main.panel2 = Ext.create('widget.panel', {
    		width: '100%',
    		//width: '500',
    		height: 200,
    		 
             
            layout: 'fit',
           /* tbar: [{
                text: 'Save Chart' 
               // handler: function(){ downloadChart(chart1); }
            }],*/
            items: [main.table]
        });
    	
    	main.panel3 = Ext.create('widget.panel', {
    		width: '100%',
    		//width: '500',
    		 
    		height: 400,
            title: main.title_panel,             
            layout: 'fit',          
            items: [main.chartAvg]
	    	
        });
    	
    	main.panelColumn = Ext.create('widget.panel',{
    		
    		layout : 'column',
    		// width: '500',
    		 
    		width: '100%',
    		height: 400,
    		border : false,
    		items : [
    		    {
    		    	columnWidth : .65,
    		    	//columnWidth : 1,
    		    	border : false,
    		    	items : [main.panel1]
    		    } ,
    		  {
    		    	columnWidth : .35,
    		    	border : false,
    		    	items : [main.panel3]
    		    } 
    		]
    	});
    	this.items = [main.panelColumn,main.panel2];
    	
    	 this.callParent();
    }


});
