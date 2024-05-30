//No uso de heranca reutilizamos classes para evitar a reescrita de código

PessoaFisica pf = new PessoaFisica();
pf.Cpf = "888.558.556-50";
pf.Endereco = "Rua dos bobos";
pf.Situacao = true;
pf.Id = 1;
pf.LerEndereco("Rua ok");

PessoaJuridica pj = new PessoaJuridica ();
pj.Cnpj = "12.345.678/0001-10";
pj.Endereco = "Rua B";
pj.Situacao = false;
pj.Id = 1;
pj.LerEndereco("Rua teste");

Console.ReadLine();