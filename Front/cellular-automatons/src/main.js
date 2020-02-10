import Vue from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue';
import VueRouter from 'vue-router';
import routes from './routes';
//import VueAxios from 'vue-axios';
//import axios from './apiConfig';
import {store} from './store';

Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(VueRouter);
//Vue.use(VueAxios, axios);

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
