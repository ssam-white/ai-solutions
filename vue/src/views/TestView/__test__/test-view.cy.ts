import { mount } from '@cypress/vue'
import TestView from '../TestView.vue'

describe('<TestView>', () => {
  beforeEach(() => {
    // cy.viewport(800, 600)
  })

  it('mounts', () => {
    mount(TestView, {
      props: {
        //
      },
    })
  })
})
