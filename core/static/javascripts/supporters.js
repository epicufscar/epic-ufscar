$(".btn-go-support, .link-talker").on("click", function () {
    if($(this).data("action") == "OUTRO") {
        $("#subject").val("DOAÇÃO");
        $("#message").val("Olá, \n\n" +
        "Gostaria de fazer uma doação para ajudar com as atividades da EPiC!");
    }
});
