clouderp.define('website_sale_options.website_sale', function(require) {
"use strict";

var ajax = require('web.ajax');
var website = require('website.website');
var base = require('web_editor.base');
require('website_sale.website_sale');

if(!$('.js_add_cart_variants[data-attribute_value_ids]').length) {
    return $.Deferred().reject("DOM doesn't contain '.js_add_cart_variants[data-attribute_value_ids]'");
}

$('.oe_website_sale #add_to_cart, .oe_website_sale #products_grid .a-submit')
    .off('click')
    .removeClass('a-submit')
    .click(function (event) {
        var $form = $(this).closest('form');
        var quantity = parseFloat($form.find('input[name="add_qty"]').val() || 1);
        var product_id = parseInt($form.find('input[type="hidden"][name="product_id"], input[type="radio"][name="product_id"]:checked').first().val(),10);
        event.preventDefault();
        ajax.jsonRpc("/shop/modal", 'call', {
                'product_id': product_id,
                'kwargs': {
                   'context': _.extend({'quantity': quantity}, base.get_context())
                },
            }).then(function (modal) {
                var $modal = $(modal);

                $modal.find('img:first').attr("src", "/web/image/product.product/" + product_id + "/image_medium");

                $modal.appendTo($form)
                    .modal()
                    .on('hidden.bs.modal', function () {
                        $(this).remove();
                    });

                $modal.on('click', '.a-submit', function () {
                    var $a = $(this);
                    $form.ajaxSubmit({
                        url:  '/shop/cart/update_option',
                        data: {lang: base.get_context().lang},
                        success: function (quantity) {
                            if (!$a.hasClass('js_goto_shop')) {
                                window.location.href = window.location.href.replace(/shop([\/?].*)?$/, "shop/cart");
                            }
                            var $q = $(".my_cart_quantity");
                            $q.parent().parent().removeClass("hidden", !quantity);
                            $q.html(quantity).hide().fadeIn(600);
                        }
                    });
                    $modal.modal('hide');
                });

                $modal.on("click", "a.js_add, a.js_remove", function (event) {
                    event.preventDefault();
                    var $parent = $(this).parents('.js_product:first');
                    $parent.find("a.js_add, span.js_remove").toggleClass("hidden");
                    $parent.find("input.js_optional_same_quantity").val( $(this).hasClass("js_add") ? 1 : 0 );
                    var $remove = $parent.find(".js_remove");
                });

                $modal.on("change", "input.js_quantity", function () {
                    var qty = parseFloat($(this).val());
                    if (qty === 1) {
                        $(".js_remove .js_items").addClass("hidden");
                        $(".js_remove .js_item").removeClass("hidden");
                    } else {
                        $(".js_remove .js_items").removeClass("hidden").text($(".js_remove .js_items:first").text().replace(/[0-9.,]+/, qty));
                        $(".js_remove .js_item").addClass("hidden");
                    }
                });

                $modal.find('input[name="add_qty"]').val(quantity).change();
                $('.js_add_cart_variants').each(function () {
                    $('input.js_variant_change, select.js_variant_change', this).first().trigger('change');
                    });

                    $modal.on("change", 'input[name="add_qty"]', function (event) {
                        var product_id = $($modal.find('span.oe_price[data-product-id]')).first().data('product-id');
                        var default_price = parseInt($('.text-danger.oe_default_price > span.oe_currency_value').text());
                        var $dom = $(event.target).closest('tr');
                        var qty = $dom.find('input[name="add_qty"]').val();
                        var product_ids = [product_id];
                        var $products_dom = [];
                        $modal.find(".js_add_cart_variants[data-attribute_value_ids]").each(function(){
                            var $el = $(this);
                            $products_dom.push($el);
                            _.each($el.data("attribute_value_ids"), function (values) {
                                product_ids.push(values[0]);
                            });
                        });
                });
            });
        return false;
    });

});
