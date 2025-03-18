import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import * as Cronitor from "@cronitorio/cronitor-rum";
import VueGtagPlugin from "vue-gtag";


const clientKey = import.meta.env.VITE_CRONITOR_CLIENT_KEY;
const gTag = import.meta.env.VITE_GTAG_MEASUREMENT_ID;

Cronitor.load(clientKey);

const app = createApp(App);

app.use(VueGtagPlugin, {
  config: { id: gTag }
})

app.mount('#app')
