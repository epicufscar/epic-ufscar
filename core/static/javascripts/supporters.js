$(".btn-go-support").on("click", function () {
    console.log($(this).data("action"));
    if($(this).data("action") != "DOAÇÃO") {
        $("#subject").val($(this).data("action"));
        $("#message").val("Olá, \n\n" +
            "Gostaria de apoiar a EPiC com suas atividades por meio do PLANO " + $(this).data("action") + ".");
    }
    else {
        $("#subject").val($(this).data("action") + " - " + $(".range-slider__value").html());

        $("#message").val("Olá, \n\n" +
            "Gostaria de doar o valor de " + $(".range-slider__value").html() +
            " para ajudar nas atividades da EPiC!");
    }
});
