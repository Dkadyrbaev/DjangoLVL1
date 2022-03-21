from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from adminapp.forms import ShopUserAdminEditForm, ProductEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render, reverse
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class UsersListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return ShopUser.objects.all().order_by('username')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        context['title'] = 'админка/пользователи'
        return context

    # def get_queryset(self):
    #     return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админ/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list,
#     }
#
#     return render(request, 'adminapp/users.html', context)


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context['title'] = 'пользователи/создание'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'user_form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)

class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data()
        context['title'] = 'пользователи/редактирование'
        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    # form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     context = {
#         'title': title,
#         'user_to_delete': user,
#     }
#
#     return render(request, 'adminapp/user_delete.html', context)


class CategoryListView(LoginRequiredMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['title'] = 'админ/категории'
        return context

    def get_queryset(self):
        return ProductCategory.objects.all()


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админ/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     content = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', content)

class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        context['title'] = 'категории/создание'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = 'категории/создание'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#
#     context = {
#         'title': title,
#         'category_form': category_form
#     }
#
#     return render(request, 'adminapp/category_update.html', context)

class CategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data()
        context['title'] = 'категории/редактирование'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'категории/редактирование'
#
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_category)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_form.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_category)
#
#     context = {
#         'title': title,
#         'category_form': edit_form
#     }
#
#     return render(request, 'adminapp/category_update.html', context)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('admin_staff:categories')
    template_name = 'adminapp/category_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data()
        context['title'] = 'категории/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'категории/удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     context = {
#         'title': title,
#         'category_to_delete': category,
#     }
#
#     return render(request, 'adminapp/category_delete.html', context)


# class ProductListView(ListView):
#     model = Product
#     template_name = 'adminapp/products.html'
#     context_object_name = 'objects'
#
#     def get_queryset(self):
#         return Product.objects.order_by('-is_active')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ProductListView, self).get_context_data()
#         context["title"] = 'продукты'
#
#         return context


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'товары/создание'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#
#     context = {
#         'title': title,
#         'product_form': product_form,
#         'category': category,
#     }
#
#     return render(request, 'adminapp/product_update.html', context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_staff:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data()
        context['title'] = 'продукт/создание'

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'продукт/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#     context = {'title': title, 'object': product, }
#
#     return render(request, 'adminapp/product_read.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        title = 'продукт'
        context.update({'title': title})

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'продукт/редактирование'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     context = {'title': title,
#                'product_form': edit_form,
#                }
#
#     return render(request, 'adminapp/product_update.html', context)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_staff:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data()
        context['title'] = 'продукт/редактирование'

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))
#
#     context = {'title': title,
#                'product_to_delete': product,
#                }
#
#     return render(request, 'adminapp/product_delete.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin_staff:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data()
        context['title'] = 'продукт/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

