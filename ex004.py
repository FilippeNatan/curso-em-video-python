var = input('Digite algo:')
print('Você digitou {}. O seu tipo primitivo é: {} '
      '\n{} é um numérico? {} '
      '\n{} é alfabético? {} '
      '\n{} é alfanumérico? {} '
      '\n{} é decimal? {} '
      '\n{} só tem espaços? {} '
      '\n{} está em maiúsculas? {} '
      '\n{} está em minúsculas? {} '
      '\n{} está capitalizada? {}'.format(var, type(var),
                                        var, var.isnumeric(),
                                        var, var.isalpha(),
                                        var, var.isalnum(),
                                        var, var.isdecimal(),
                                        var, var.isspace(),
                                        var, var.isupper(),
                                        var, var.islower(),
                                        var, var.istitle()))
