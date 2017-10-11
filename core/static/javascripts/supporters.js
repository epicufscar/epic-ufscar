$(".btn-go-support, .link-talker").on("click", function () {
    if($(this).data("action") == "OUTRO") {
        $("#subject").val("DOAÇÃO");
        $("#message").val("Olá, \n\n" +
        "Gostaria de fazer uma doação no valor de " + $(".range-slider__value").html() + " para ajudar com as atividades da EPiC!");
    }
    else {
        $("#subject").val($(this).data("action"));
        $("#message").val("Olá, \n\n" +
            "Gostaria de apoiar a EPiC com suas atividades por meio do PLANO " + $(this).data("action") + ".");
    }
});
