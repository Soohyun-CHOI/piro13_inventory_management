from django.shortcuts import render, redirect

from inventory.models import Item


def item_list(request):
    items = Item.objects.all()
    ctx = {
        "items": items
    }
    return render(request, "inventory/item_list.html", ctx)


def item_read(request, pk):
    item = Item.objects.get(pk=pk)
    ctx = {
        "item": item
    }
    return render(request, "inventory/item_read.html", ctx)


def item_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.POST.get("image")
        content = request.POST.get("content")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        # account

        item = Item.objects.create(
            title=title, image=image, content=content, price=price, amount=amount
        )
        return redirect("item_read", item.pk)

    return render(request, "inventory/item_create.html")


def item_update(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == "GET":
        ctx = {
            "item": item
        }
        return render(request, "inventory/update.html", ctx)

    elif request.method == "POST":
        title = request.POST["title"]
        image = request.POST["image"]
        content = request.POST["content"]
        price = request.POST["price"]
        amount = request.POST["amount"]
        #account

        item.title = title
        item.image = image
        item.content = content
        item.price = price
        item.amount = amount

        return redirect("item_read", item.pk)


def item_delete(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == "GET":
        return redirect("item_read", item.pk)

    elif request.method == "POST":
        item.delete()
        return redirect("item_list")
