import DefaultTheme from 'vitepress/theme'
import GuideHome from './GuideHome.vue'
import './custom.css'
export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('GuideHome', GuideHome)
  }
}
