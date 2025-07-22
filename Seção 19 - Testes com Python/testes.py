import unittest

from atividades import comer, dormir, eh_engracada, divide

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )
    
    def test_come_gostosa(self):
        """Testando o retorno com comiga gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormingo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormingo muito."""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )
    
    def test_eh_engracada(self):
        # self.assertEqual(eh_engracada('Sérgio Malandro'), False) # Enquando a função não está implementada é preciso executar este, pois a outra sempre retorna False
        self.assertFalse(eh_engracada('Sérgio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado') # A mensagem personalizada é o que aparece no erro

    def test_divide(self):
        self.assertIsNot(divide(5, 0),'O segundo valor deve ser diferente de 0, caso contrário, não é possível realizar a divisão!')


if __name__ == '__main__':
    unittest.main()
