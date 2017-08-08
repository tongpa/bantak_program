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
     
    	var addRisk  = Ext.create('ChartGraph', {
    		title_panel : 'เวลาในการจัดทำสรุปรายงาน', 
    		storeChart : question.storeCompair 
    	}); 
    	 
    	var addRisk2  = Ext.create('ChartGraph', {
    		title_panel : 'เวลาในการจัดแยกรายงานเพื่อนำส่งและตอบกลับของหน่วยงาน',
    		storeChart : question.storeCompair2 
    	});
    	var addRisk3  = Ext.create('ChartGraph', {
    		title_panel : 'เวลาในการรวบรวมเอกสาร', 
    		storeChart : question.storeCompair3 
    	});
    	var addRisk4  = Ext.create('ChartGraph', {
    		title_panel : ' เวลาในการแปรผลข้อมูล',  
    		storeChart : question.storeCompair4 
    	});
    	var addRisk5  = Ext.create('ChartGraph', {
    		title_panel : 'ลดขั้นตอนการทำงาน',  
    		storeChart : question.storeCompair5 
    	});
    	var addRisk6  = Ext.create('ChartGraph', {
    		title_panel : 'ประมวลผลรวดเร็ว ถูกต้อง แม่นยำ',  
    		storeChart : question.storeCompair6 
    	});
    	//////////////////////
    	var addRisk7  = Ext.create('ChartGraph', {
    		title_panel : 'เข้าถึงข้อมูล/สรุปรายงานได้อย่างสะดวก',  
    		storeChart : question.storeCompair7 
    	});
    	var addRisk8  = Ext.create('ChartGraph', {
    		title_panel : 'ค้นหารายงานอุบัติการณ์เก่าได้',  
    		storeChart : question.storeCompair8 
    	});
    	var addRisk9  = Ext.create('ChartGraph', {
    		title_panel : 'การใช้งานของระบบง่าย',  
    		storeChart : question.storeCompair9 
    	});
    	var addRisk10  = Ext.create('ChartGraph', {
    		title_panel : 'ข้อความที่แสดงสื่อความหมายชัดเจน   (ลายมือ)',  
    		storeChart : question.storeCompair10 
    	});
    	var addRisk11  = Ext.create('ChartGraph', {
    		title_panel : 'ความปลอดภัยในการเข้าถึงระบบ',  
    		storeChart : question.storeCompair11 
    	});
    	var addRisk12  = Ext.create('ChartGraph', {
    		title_panel : 'คู่มือการใช้งานชัดเจน',  
    		storeChart : question.storeCompair12 
    	});
    	var addRisk13  = Ext.create('ChartGraph', {
    		title_panel : 'การรายงายผลของข้อมูล มีความชัดเจน ถูกต้อง สมบูรณ์ ครบถ้วน ',  
    		storeChart : question.storeCompair13 
    	});
    	///////////////////
    	var addRisk14  = Ext.create('ChartGraph', {
    		title_panel : 'ความสิ้นเปลืองของการใช้กระดาษ',  
    		storeChart : question.storeCompair14 
    	});
    	var addRisk15  = Ext.create('ChartGraph', {
    		title_panel : 'ความสิ้นเปลืองของการใช้หมึกพิมพ์',  
    		storeChart : question.storeCompair15 
    	});
    	var addRisk16  = Ext.create('ChartGraph', {
    		title_panel : 'ความสิ้นเปลืองเนื้อที่ในการเก็บเอกสาร',  
    		storeChart : question.storeCompair16 
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