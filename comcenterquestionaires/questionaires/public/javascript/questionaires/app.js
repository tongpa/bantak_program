Ext.Loader.setConfig({enabled: true});
//Ext.Loader.setPath('Ext.ux', '/ux');

Ext.Loader.setPath('Ext.ux', '/javascript/extjs/examples/ux');
Ext.Loader.setPath('question', '/javascript/questionaires');
Ext.require([
             
             'Ext.form.*',
             'Ext.layout.container.Column',
             'Ext.ux.form.MultiSelect',
             'Ext.ux.form.ItemSelector',
             'Ext.tip.QuickTipManager',
             'Ext.ux.ajax.JsonSimlet',
             'Ext.ux.ajax.SimManager',             
             'Ext.window.MessageBox'
             
         ]);
 
Ext.application({
    name: 'question',
    launch: function() {
    	Ext.tip.QuickTipManager.init();
      
    	question.storeCompair.load();
    	question.storeCompair2.load();
    	question.storeCompair3.load();
    	question.storeCompair4.load();
    	question.storeCompair5.load();
    	question.storeCompair6.load();
    	question.storeCompair7.load();
    	question.storeCompair8.load();
    	question.storeCompair9.load();
    	question.storeCompair10.load();
    	question.storeCompair11.load();
    	question.storeCompair12.load();
    	question.storeCompair13.load();
    	question.storeCompair14.load();
    	question.storeCompair15.load();
    	question.storeCompair16.load();
    	 

    	question.storeCompairAvg16.load();
    	question.storeCompairAvg.load(); 
    	question.storeCompairAvg2.load();
    	question.storeCompairAvg3.load();
    	question.storeCompairAvg4.load();
    	question.storeCompairAvg5.load();
    	question.storeCompairAvg6.load();
    	question.storeCompairAvg7.load();
    	question.storeCompairAvg8.load();
    	question.storeCompairAvg9.load();
    	question.storeCompairAvg10.load();
    	question.storeCompairAvg11.load();
    	question.storeCompairAvg12.load();
    	question.storeCompairAvg13.load();
    	question.storeCompairAvg14.load();
    	question.storeCompairAvg15.load();
    	 
    	var addRisk  = Ext.create('ChartGraph', {
    		title_panel : 'เวลาในการจัดทำสรุปรายงาน', 
    		storeChart : question.storeCompair ,
    		storeChartAvg : question.storeCompairAvg
    	}); 
    	 
    	var addRisk2  = Ext.create('ChartGraph', {
    		title_panel : 'เวลาในการจัดแยกรายงานเพื่อนำส่งและตอบกลับของหน่วยงาน',
    		storeChart : question.storeCompair2 ,
    		storeChartAvg : question.storeCompairAvg2
    	});
    	var addRisk3  = Ext.create('ChartGraph', {
    		title_panel : 'เวลาในการรวบรวมเอกสาร', 
    		storeChart : question.storeCompair3 ,
    		storeChartAvg : question.storeCompairAvg3
    	});
    	var addRisk4  = Ext.create('ChartGraph', {
    		title_panel : ' เวลาในการแปรผลข้อมูล',  
    		storeChart : question.storeCompair4 ,
    		storeChartAvg : question.storeCompairAvg4
    	});
    	var addRisk5  = Ext.create('ChartGraph', {
    		title_panel : 'ลดขั้นตอนการทำงาน',  
    		storeChart : question.storeCompair5 ,
    		storeChartAvg : question.storeCompairAvg5
    	});
    	var addRisk6  = Ext.create('ChartGraph', {
    		title_panel : 'ประมวลผลรวดเร็ว ถูกต้อง แม่นยำ',  
    		storeChart : question.storeCompair6 ,
    		storeChartAvg : question.storeCompairAvg6
    	});
    	//////////////////////
    	var addRisk7  = Ext.create('ChartGraph', {
    		title_panel : 'เข้าถึงข้อมูล/สรุปรายงานได้อย่างสะดวก',  
    		storeChart : question.storeCompair7 ,
    		storeChartAvg : question.storeCompairAvg7
    	});
    	var addRisk8  = Ext.create('ChartGraph', {
    		title_panel : 'ค้นหารายงานอุบัติการณ์เก่าได้',  
    		storeChart : question.storeCompair8 ,
    		storeChartAvg : question.storeCompairAvg8
    	});
    	var addRisk9  = Ext.create('ChartGraph', {
    		title_panel : 'การใช้งานของระบบง่าย',  
    		storeChart : question.storeCompair9 ,
    		storeChartAvg : question.storeCompairAvg9
    	});
    	var addRisk10  = Ext.create('ChartGraph', {
    		title_panel : 'ข้อความที่แสดงสื่อความหมายชัดเจน   (ลายมือ)',  
    		storeChart : question.storeCompair10 ,
    		storeChartAvg : question.storeCompairAvg10
    	});
    	var addRisk11  = Ext.create('ChartGraph', {
    		title_panel : 'ความปลอดภัยในการเข้าถึงระบบ',  
    		storeChart : question.storeCompair11 ,
    		storeChartAvg : question.storeCompairAvg11
    	});
    	var addRisk12  = Ext.create('ChartGraph', {
    		title_panel : 'คู่มือการใช้งานชัดเจน',  
    		storeChart : question.storeCompair12 ,
    		storeChartAvg : question.storeCompairAvg12
    	});
    	var addRisk13  = Ext.create('ChartGraph', {
    		title_panel : 'การรายงายผลของข้อมูล มีความชัดเจน ถูกต้อง สมบูรณ์ ครบถ้วน ',  
    		storeChart : question.storeCompair13 ,
    		storeChartAvg : question.storeCompairAvg13
    	});
    	///////////////////
    	var addRisk14  = Ext.create('ChartGraph', {
    		title_panel : 'ความสิ้นเปลืองของการใช้กระดาษ',  
    		storeChart : question.storeCompair14 ,
    		storeChartAvg : question.storeCompairAvg14
    	});
    	var addRisk15  = Ext.create('ChartGraph', {
    		title_panel : 'ความสิ้นเปลืองของการใช้หมึกพิมพ์',  
    		storeChart : question.storeCompair15 ,
    		storeChartAvg : question.storeCompairAvg15
    	});
    	var addRisk16  = Ext.create('ChartGraph', {
    		title_panel : 'ความสิ้นเปลืองเนื้อที่ในการเก็บเอกสาร',  
    		storeChart : question.storeCompair16 ,    		
    		storeChartAvg : question.storeCompairAvg16
    	});
    	 
    	
    	 
    	
    	Ext.create('Ext.tab.Panel',{
    		renderTo : 'maintenance-app',
    		items : [ addRisk,addRisk2,addRisk3,addRisk4,addRisk5,addRisk6 ,
    		          addRisk7,addRisk8,addRisk9,addRisk10,addRisk11,addRisk12 ,addRisk13
    		          ,addRisk14,addRisk15 ,addRisk16
    		          ]
    	});
    	
    	 
    	 
    }
});