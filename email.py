import emails as emails

message = emails.html(html="<p>Hi!<br>Here is your receipt...",
                      subject="Your EMAIL FROM PYTHON SCRIPT",
                      mail_from=('Shreeja', 'shree@xyz.com'))
mail_via_python = message.send(to='gaseniy838@boersy.com',
                               smtp={'host': 'smtp.gmail.com', 'timeout': 5, 'port': 587,
                                     'user': 'shreejakale18@gmail.com',
                                     'password': 's2107',
                                     'tls': True})

