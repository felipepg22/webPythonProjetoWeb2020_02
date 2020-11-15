$('#id_produto').change(function(e){

    let id_produto = e.target.value;

    $.post($SCRIPT_ROOT + "{{ url_for('pedidos.buscaProdutoById') }}", {

        id_produto:id_produto
    }, function(data){

        if(!data.erro){

            let produto = $.parseJSON(data.produto);

            $('#imagemProduto').attr('src', produto.imagem);
            $('#valor').val(produto.valor);
            $('#quantidade').val(1);
            $('#total').val(1 * produto.valor);
        }
        else{

            console.log(data.mensagem_exception);
        }
    })
});

$('#id_cliente').keyup(function(e){

    let id_cliente = e.target.value; // Pega o que está sendo digitado no input
    $.post($SCRIPT_ROOT + "{{ url_for('pedidos.buscaClienteById') }}", {

        id_cliente:id_cliente
    }, function(data){

        if(data.erro){

            console.log(data.mensagem_exception);
        }

        else if(data.cliente_encontrado){
            // Preenche os campos de cliente do formulário
            let cliente = $.parseJSON(data.cliente);
            $('#nomeCliente').val(cliente.nome);
            $('#telefone').val(cliente.telefone);
            $('#endereco').val(cliente.endereco);
            $('#numeroEndereco').val(cliente.numero);
            $('#cep').val(cliente.cep);
            $('#bairro').val(cliente.bairro);
            $('#cidade').val(cliente.cidade);
        }

        else{
            $('#nomeCliente').val("");
            $('#telefone').val("");
            $('#endereco').val("");
            $('#numeroEndereco').val("");
            $('#cep').val("");
            $('#bairro').val("");
            $('#cidade').val("");
        }
    })
})

$('#addPedido').submit(function(e){

    e.preventDefault();

    $.post($SCRIPT_ROOT + "{{ url_for('pedidos.addPedido') }}", {

        id_cliente: $('#id_cliente').val(),
        data_hora: $('#data_hora').val(),
        observacao: $('#observacao').val()

    }, function(data){

        if(!data.erro){

            swal(data.mensagem, '', 'success');

            setTimeout(function(){

                window.location.replace($SCRIPT_ROOT + "{{ url_for('pedidos.formListaPedidos') }}");
            }, 1000)
        }

        else{
            swal(data.mensagem, '', 'error');
            console.log(data.mensagem_exception);
        }
    })
})

$('#addProdutoPedido').click(function(e){

    $.post($SCRIPT_ROOT + "{{ url_for('pedidos.addProdutoPedido') }}", {

        id_pedido: $('#id_pedido').val(),
        id_produto: $('#id_produto').val(),
        quantidade: $('#quantidade').val(),
        valor: $('#valor').val(),
        observacao:$('#observacoesProduto').val()
    }, function(data){

        if(!data.erro){

            swal(data.mensagem, '', 'success');

            
        }
        else{
            swal(data.mensagem, '', 'error');
            console.log(data.mensagem_exception);
        }
    })
})

$('#quantidade').change(function(e){

    let valor_produto = $('#valor').val();

    $('#total').val(e.target.value * valor_produto);
})