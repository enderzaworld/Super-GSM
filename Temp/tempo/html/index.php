<!DOCTYPE html>
<html style="height:100%;">
<head>
	<title>
		control
	</title>
	<script type="text/javascript" src="jquery-3.1.1.min.js"></script>
</head>
<body style="min-height:100%;">
	<table id="table1" style="height:100%;width:100%;">
		<tr style="height:30%;width:100%;">
			<td style="height:33%;width:33%;">
				<button id="btn-1" style="height:100%;width:100%;">LF</button>
			</td>
			<td style="height:33%;width:33%;">
				<button id="btn-2" style="height:100%;width:100%;">FF</button>
			</td>
			<td style="height:33%;width:33%;">
				<button id="btn-3" style="height:100%;width:100%;">RF</button>
			</td>
		</tr>
		<tr style="height:30%;width:100%;">
			<td style="height:33%;width:33%;">
				<button id="btn-4" style="height:100%;width:100%;">LL</button>
			</td>
			<td style="height:33%;width:33%;">
                                <button id="btn-0" style="height:100%;width:100%;">REST</button>				
			</td>
			<td style="height:33%;width:33%;">
				<button id="btn-5" style="height:100%;width:100%;">RR</button>
			</td>
		</tr>
		<tr style="height:30%;width:100%;">
			<td style="height:33%;width:33%;">
				<button id="btn-6" style="height:100%;width:100%;">LB</button>
			</td>
			<td style="height:33%;width:33%;">
				<button id="btn-7" style="height:100%;width:100%;">BB</button>
			</td>
			<td style="height:33%;width:33%;">
				<button id="btn-8" style="height:100%;width:100%;">RB</button>
			</td>
		</tr>
	</table>
	<script>	
$( "button[id^='btn-']" )
  .mousedown(function() {
	var str = $(this).attr('id').split("-")[1];
	$.get( "writer.php", { "number": str } );
  })
  .mouseup(function() {
	$.get( "writer.php", { "number": 0 } );
  });
$(document).ready(function(){
    var b= $(window).height();
    $("#table1").css("height",b);
});
	</script>
</body>
</html>
