$(function () {
	$('.plans-item .plan-card').removeClass('active');
	$('.plans-item:eq(0) .plan-card').addClass('active');



	function noZero(_data) {
		if(_data == '' || _data == undefined) {
			_data = '0';
			return _data;
		}
		else{
			return _data;
		}
	}

	function calc(amount,percent,daily){
		var daily_profit = amount/100*daily;
		var total_profit = amount/100*percent;
		var profit_d = daily_profit.toFixed(2);
		var profit_t = total_profit.toFixed(2);
		$("#daily").text(profit_d + "$");
		$("#profit").text(profit_t + "$");
	}

	function selectPlan() {

		$('.plans-list').each(function () {
			var current = $(this).find('.plans-item:eq(0) .plan-card'),
					data1 = current.data('percent'),
					data2 = current.data('min'),
					data3 = current.data('max'),
					data4 = current.data('deposit'),
					data7 = current.data('term'),
					data8 = current.data('daily');

			$('#percent').html(noZero(data1));
			$('#term').html(noZero(data7));
			$('#min').html(noZero(data2));
			$('#max').html(noZero(data3));
			$("#deposit").html(noZero(data4));
			$('#range-min').html(noZero(data2));
			$('#range-max').html(noZero(data3));

			$("#amount").text(data2  + "$");
			$('#slider-range').slider({
				range: "min",
				value: data2,
				min: data2,
				max: data3,
				slide: function slide(event, ui) {
					$("#amount").text(ui.value + "$");
				}
			});
			calc(data2,data1,data8);
		});

		$('.plans-item .plan-card').click(function () {
			$('.plans-item .plan-card').removeClass('active');
			$(this).addClass('active');
			var current = $(this);
			var data1 = current.data('percent'),
					data2 = current.data('min'),
					data3 = current.data('max'),
					data4 = current.data('deposit'),
					data7 = current.data('term'),
					data8 = current.data('daily');

			$('#percent').html(noZero(data1));
			$('#term').html(noZero(data7));
			$('#min').html(noZero(data2));
			$('#max').html(noZero(data3));
			$("#deposit").html(data4);
			$('#range-min').html(noZero(data2));
			$('#range-max').html(noZero(data3));
			$("#amount").text(data2 + "$");

			$( "#slider-range" ).slider("option","min", data2);
			$( "#slider-range" ).slider("option","max", data3);
			$( "#slider-range" ).slider("option","value", data2);
			calc(data2,data1,data8);
		});

		$( "#slider-range" ).on( "slide", function( event, ui ) {
			var planSelected = $('.plans-item .plan-card.active');
			var amount = ui.value,
					daily = planSelected.data('daily'),
					percent = planSelected.data('percent');
			calc(amount,percent,daily);
		});


	}

	selectPlan();
});