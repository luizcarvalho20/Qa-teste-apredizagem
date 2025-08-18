describe('Login', () => {
  it('exibe erro com senha inválida', () => {
    cy.visit('/login');
    cy.get('#username').type('tomsmith');
    cy.get('#password').type('wrongPassword');
    cy.get('button[type=submit]').click();
    cy.contains('Your password is invalid!').should('be.visible');
  });
});
