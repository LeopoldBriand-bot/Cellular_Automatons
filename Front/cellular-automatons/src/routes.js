import presentation from './components/presentation.vue'
import boids from './components/boids.vue'
import cristal from './components/cristal.vue'

const routes = [
    { path: '/', redirect: {name: 'Presentation'}},
    { path: '/presentation', component: presentation, name: 'Presentation'},
    { path: '/boids', component: boids, name: 'Boids'},
    { path: '/cristal', component: cristal, name: 'Cristal'},
]

export default routes