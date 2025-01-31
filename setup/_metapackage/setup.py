import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-product-attribute",
    description="Meta package for oca-product-attribute Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-packaging_uom',
        'odoo13-addon-product_abc_classification',
        'odoo13-addon-product_assortment',
        'odoo13-addon-product_attribute_archive',
        'odoo13-addon-product_attribute_value_menu',
        'odoo13-addon-product_barcode_required',
        'odoo13-addon-product_bom_revision',
        'odoo13-addon-product_category_active',
        'odoo13-addon-product_category_code',
        'odoo13-addon-product_code_mandatory',
        'odoo13-addon-product_code_unique',
        'odoo13-addon-product_cost_security',
        'odoo13-addon-product_custom_info',
        'odoo13-addon-product_dimension',
        'odoo13-addon-product_dimension_volumetric_weight',
        'odoo13-addon-product_list_pricelist_price',
        'odoo13-addon-product_lot_sequence',
        'odoo13-addon-product_manufacturer',
        'odoo13-addon-product_medical',
        'odoo13-addon-product_multi_category',
        'odoo13-addon-product_multi_price',
        'odoo13-addon-product_order_noname',
        'odoo13-addon-product_packaging_dimension',
        'odoo13-addon-product_packaging_type',
        'odoo13-addon-product_packaging_type_pallet',
        'odoo13-addon-product_packaging_type_required',
        'odoo13-addon-product_packaging_unit_price_calculator',
        'odoo13-addon-product_pricelist_assortment',
        'odoo13-addon-product_pricelist_button_box',
        'odoo13-addon-product_pricelist_by_contact',
        'odoo13-addon-product_pricelist_direct_print',
        'odoo13-addon-product_pricelist_direct_print_website_sale',
        'odoo13-addon-product_pricelist_revision',
        'odoo13-addon-product_pricelist_supplierinfo',
        'odoo13-addon-product_product_template_navigation',
        'odoo13-addon-product_restricted_type',
        'odoo13-addon-product_secondary_unit',
        'odoo13-addon-product_sequence',
        'odoo13-addon-product_state',
        'odoo13-addon-product_stock_state',
        'odoo13-addon-product_supplierinfo_archive',
        'odoo13-addon-product_supplierinfo_for_customer',
        'odoo13-addon-product_supplierinfo_revision',
        'odoo13-addon-product_template_tags',
        'odoo13-addon-product_template_tags_code',
        'odoo13-addon-product_total_weight_from_packaging',
        'odoo13-addon-product_uom_updatable',
        'odoo13-addon-product_variant_attribute_name_manager',
        'odoo13-addon-product_weight',
        'odoo13-addon-stock_account_product_cost_security',
        'odoo13-addon-stock_production_lot_firmware_version',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
