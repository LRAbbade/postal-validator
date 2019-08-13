const validateRoute = 'http://localhost:5000/validate';

$("#validate-btn").click(() => {
    const cep = $('#cep').val();
    console.log(`Checking cep ${cep}`);

    $.ajax({
        url: validateRoute + '?cep=' + cep,
        type: 'GET',
        beforeSend: () => {
            $("#validate-btn").attr("disabled", true);
        },
        success: (res) => {
            console.log(`Received results: ${JSON.stringify(res)}`);
            var text = `Cep ${res.cep} é `;
            text += res.result ? 'válido' : 'inválido';

            $("#result").text(text);
            $("#results-div").removeAttr('hidden');
        },
        error: () => {
            alert(`Erro ao consultar cep "${cep}"`);
        },
        complete: () => {
            $("#validate-btn").attr("disabled", false);
        }
    });
});
