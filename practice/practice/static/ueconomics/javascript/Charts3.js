var mode = 'lines';
var last_product_chosen = null;
var clicked_btns = []
clicked_btns.push(document.getElementById('lines-btn'))

function reset_btns_colors() {
    for (var i = 0; i < clicked_btns.length; i++) {
        clicked_btns[i].style.color = 'black';
    }
}

function change_chart_type(event, type) {
//alert(type)
    reset_btns_colors();

    var clicked_btn = event.target;
    clicked_btns.push(clicked_btn);
    clicked_btn.style.color = "blue";
    mode = type;

    var event_ = new Event("click", { bubbles: true });
    if (last_product_chosen !== null) {
        last_product_chosen.dispatchEvent(event_);
    }
}


get_chart_data = function(event){
     var elm = event.target;
     //alert(elm.innerHTML)
     last_product_chosen = event.target;
     var title_ = elm.innerHTML;
     //alert(title_)
     var id = elm.getAttribute("id");
     var data = elm.parentNode;
     //alert(data.outerHTML)

     var exp_id = 'exports_'+id.split("_")[1];
//     alert(exp_id)

     var imp_id = 'imports_'+id.split("_")[1];
//     alert(imp_id)

     exp_data = []
     imp_data = []

    for (var i=2015; i <2020; i++) {
   eve =document.getElementById(exp_id+"_"+i).innerHTML
//   alert(eve)
   evi =document.getElementById(imp_id+"_"+i).innerHTML
   exp_data.push(eve)
   imp_data.push(evi)
}
//alert(exp_data)
//alert(imp_data)

  y = [];

  for (var i=2015; i<2020; i++){
      y.push(i)
  };
 if (mode == 'lines')

 {
    get_line_chart(title_, y, exp_data, imp_data)
  } else if (mode == 'pies')
  {
     get_pie_chart(title_, y, exp_data, imp_data)
  }else if (mode == 'histos')
  {
     get_histos_chart(title_, y, exp_data, imp_data)
  }else if (mode == 'bars')
  {
     get_bars_chart(title_, y, exp_data, imp_data)
  }

}

get_line_chart = function(title, y, exp_data, imp_data) {
//alert(title)
  var trace1 = {
  x: y,
  y: exp_data,
  type: 'line',
  name: 'exports'
};

var trace2 = {
  x: y,
  y: imp_data,
  type: 'line',
  name: 'imports'
};

var layout = { title:title}

var data = [trace1, trace2];

Plotly.newPlot('myChart', data, layout);
}


function get_pie_chart(title, y, exp_data, imp_data)
{
var data = [{
  values: exp_data,
  labels: y,
  domain: {column: 0},
  name: 'export',
  hoverinfo: 'label+percent+name',
  hole: .4,
  type: 'pie'
},{
  values:  imp_data,
  labels: y,
  text: 'CO2',
  textposition: 'inside',
  domain: {column: 1},
  name: 'import',
  hoverinfo: 'label+percent+name',
  hole: .4,
  type: 'pie'
}];

var layout = {
  title: title,
  annotations: [
    {
      font: {
        size: 20
      },
      showarrow: false,
      text: 'Export',
      x: 0.17,
      y: 0.5
    },
    {
      font: {
        size: 20
      },
      showarrow: false,
      text: 'Import',
      x: 0.82,
      y: 0.5
    }
  ],
  height: 400,
  width: 600,
  showlegend: false,
  grid: {rows: 1, columns: 2}
};

Plotly.newPlot('myChart', data, layout);
}

get_histos_chart = function(title, y, exp_data, imp_data)
{
var x1 = [];
var x2 = [];
var y1 = [];
var y2 = [];
for (var i = 1; i < 500; i++)
{
  k = Math.random();
  x1.push(k*5);
  x2.push(k*10);
  y1.push(k);
  y2.push(k*2);
}
var trace1 = {
  x: x1,
  y: y1,
  name: 'Export',
  autobinx: false,
  histnorm: "count",
  marker: {
    color: "rgba(255, 100, 102, 0.7)",
     line: {
      color:  "rgba(255, 100, 102, 1)",
      width: 1
    }
  },
  opacity: 0.5,
  type: "histogram",
  xbins: {
    end: 2.8,
    size: 0.06,
    start: .5
  }
};
var trace2 = {
  x: x2,
  y: y2,
  autobinx: false,
  marker: {
          color: "rgba(100, 200, 102, 0.7)",
           line: {
            color:  "rgba(100, 200, 102, 1)",
            width: 1
    }
       },
  name: "Import",
  opacity: 0.75,
  type: "histogram",
  xbins: {
    end: 4,
    size: 0.06,
    start: -3.2

  }
};
var data = [trace1, trace2];
var layout = {
  bargap: 0.05,
  bargroupgap: 0.2,
  barmode: "overlay",
  title: "Sampled Results",
  xaxis: {title: "Years"},
  yaxis: {title: "Value"}
};
Plotly.newPlot( myChart, data, layout);
}

get_bars_chart = function(title, y, exp_data, imp_data)
{
var trace1 = {
  x: y,
  y: exp_data,
  type: 'bar',
  name: 'Export',
  marker: {
    color: 'rgb(49,130,189)',
    opacity: 0.7,
  }
};

var trace2 = {
  x: y,
  y: imp_data,
  type: 'bar',
  name: 'Import',
  marker: {
    color: 'rgb(204,204,204)',
    opacity: 0.5
  }
};

var data = [trace1, trace2];

var layout = {
  title: title,
  xaxis: {
    tickangle: -45
  },
  barmode: 'group'
};
	Plotly.newPlot( myChart, data, layout );
}
