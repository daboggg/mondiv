import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ky from 'ky'
import messagePlugin from "@/plugins/message.plugin";
import 'materialize-css/dist/js/materialize.min'

createApp(App)
    .use(store)
    .use(router)
    .use(messagePlugin)
    .mount('#app')
