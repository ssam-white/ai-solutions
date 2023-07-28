import { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'index',
        component: () => import('pages/IndexPage.vue'),
      },
      {
        path: 'chat',
        name: 'chatBot',
        component: () => import('pages/ChatPage.vue')
      },
      {
        path: 'blip',
        name: 'blip',
        component: () => import('pages/BlipPage.vue')
      },
      {
        path: 'test',
        name: 'test',
        component: () => import('pages/TestPage.vue'),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
