import { createApp } from 'vue'
import App from './App.vue'
import Toaster from '@meforma/vue-toaster'
import router from './router'
import store from './store'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import ky from 'ky'
import messagePlugin from "@/plugins/message.plugin";

createApp(App)
    .use(store)
    .use(router)
    .use(Toaster)
    .use(messagePlugin)
    .mount('#app')
