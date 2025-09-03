from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Portfolio

class PortfolioListView(ListView):
    model = Portfolio
    template_name = "portfolio/portfolio_list.html"
    context_object_name = "portfolios"

class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    fields = ["title", "description", "screenshot", "file", "link"]
    template_name = "portfolio/portfolio_form.html"
    success_url = reverse_lazy("portfolio_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PortfolioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Portfolio
    fields = ["title", "description", "screenshot", "file", "link"]
    template_name = "portfolio/portfolio_form.html"
    success_url = reverse_lazy("portfolio_list")

    def test_func(self):
        return self.get_object().user == self.request.user

class PortfolioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Portfolio
    template_name = "portfolio/portfolio_confirm_delete.html"
    success_url = reverse_lazy("portfolio_list")

    def test_func(self):
        return self.get_object().user == self.request.user
