import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

const app = createApp(App)

// app.use(createPinia())
app.use(pinia)

app.mount('#app')
