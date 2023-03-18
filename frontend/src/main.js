import {createApp} from 'vue'
import App from './App.vue'
import Toaster from '@meforma/vue-toaster'
import router from './router'
import store from './store'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {Vue3BsPaginate} from 'vue3-bootstrap-paginate'
import ky from 'ky'
import messagePlugin from "@/plugins/message.plugin";

createApp(App)
    .use(store)
    .use(router)
    .use(Toaster)
    .use(messagePlugin)
    .component('Vue3BsPaginate', Vue3BsPaginate)
    .mount('#app')
