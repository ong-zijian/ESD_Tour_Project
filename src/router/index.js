import enquiryformViewVue from "@/views/EnquiryFormView.vue";
import { createRouter, createWebHistory, VueRouter } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/enquiry",
    name: "enquiry",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/EnquiryFormView.vue"),
  },
  {
    path: "/tourlisting",
    name: "tourlisting",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/TourListingView.vue"),
  },

  {
    path: "/orderForm/:TID/:startDateTime",
    name: "orderForm",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/OrderForm.vue"),
  },


];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
