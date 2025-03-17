import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import * as Cronitor from "@cronitorio/cronitor-rum";


const clientKey = import.meta.env.VITE_CRONITOR_CLIENT_KEY;
Cronitor.load(clientKey);

createApp(App).mount('#app')

Cronitor.track("Pageview");
