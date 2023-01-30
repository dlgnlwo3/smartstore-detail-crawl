if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from enum import Enum


class productInfoProvidedNotice(Enum):

    WEAR = {
        "productInfoProvidedNoticeType": "WEAR",
        "wear": {
            "returnCostReason": "0",  # 미입력 시 상품상세 참조
            "noRefundReason": "0",  # 미입력 시 상품상세 참조
            "qualityAssuranceStandard": "0",  # 미입력 시 상품상세 참조
            "compensationProcedure": "0",  # 미입력 시 상품상세 참조
            "troubleShootingContents": "0",  # 미입력 시 상품상세 참조
            "material": "상품상세참조",
            "color": "상품상세참조",
            "size": "상품상세참조",
            "manufacturer": "상품상세참조",
            "caution": "상품상세참조",
            # "packDate": "상품상세참조",
            "packDateText": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    SHOES = {
        "productInfoProvidedNoticeType": "SHOES",
        "shoes": {
            "returnCostReason": "0",  # 미입력 시 상품상세 참조
            "noRefundReason": "0",  # 미입력 시 상품상세 참조
            "qualityAssuranceStandard": "0",  # 미입력 시 상품상세 참조
            "compensationProcedure": "0",  # 미입력 시 상품상세 참조
            "troubleShootingContents": "0",  # 미입력 시 상품상세 참조
            "material": "상품상세참조",
            "color": "상품상세참조",
            "size": "상품상세참조",
            "height": "상품상세참조",
            "manufacturer": "상품상세참조",
            "caution": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    BAG = {
        "productInfoProvidedNoticeType": "BAG",
        "bag": {
            "returnCostReason": "0",  # 미입력 시 상품상세 참조
            "noRefundReason": "0",  # 미입력 시 상품상세 참조
            "qualityAssuranceStandard": "0",  # 미입력 시 상품상세 참조
            "compensationProcedure": "0",  # 미입력 시 상품상세 참조
            "troubleShootingContents": "0",  # 미입력 시 상품상세 참조
            "type": "상품상세참조",
            "material": "상품상세참조",
            "color": "상품상세참조",
            "size": "상품상세참조",
            "manufacturer": "상품상세참조",
            "caution": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    FASHION_ITEMS = {
        "productInfoProvidedNoticeType": "FASHION_ITEMS",
        "fashionItems": {
            "returnCostReason": "0",  # 미입력 시 상품상세 참조
            "noRefundReason": "0",  # 미입력 시 상품상세 참조
            "qualityAssuranceStandard": "0",  # 미입력 시 상품상세 참조
            "compensationProcedure": "0",  # 미입력 시 상품상세 참조
            "troubleShootingContents": "0",  # 미입력 시 상품상세 참조
            "type": "상품상세참조",
            "material": "상품상세참조",
            "size": "상품상세참조",
            "manufacturer": "상품상세참조",
            "caution": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    SLEEPING_GEAR = {
        "productInfoProvidedNoticeType": "SLEEPING_GEAR",
        "sleepingGear": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "material": "string",
            "color": "string",
            "size": "string",
            "components": "string",
            "manufacturer": "string",
            "caution": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    FURNITURE = {
        "productInfoProvidedNoticeType": "FURNITURE",
        "furniture": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "certificationType": "string",
            "color": "string",
            "components": "string",
            "material": "string",
            "manufacturer": "string",
            "importer": "string",
            "producer": "string",
            "size": "string",
            "installedCharge": "string",
            "warrantyPolicy": "string",
            "refurb": "string",
            "afterServiceDirector": "string",
        },
    }

    IMAGE_APPLIANCES = {
        "productInfoProvidedNoticeType": "IMAGE_APPLIANCES",
        "imageAppliances": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "ratedVoltage": "string",
            "powerConsumption": "string",
            "energyEfficiencyRating": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "size": "string",
            "additionalCost": "string",
            "displaySpecification": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    HOME_APPLIANCES = {
        "productInfoProvidedNoticeType": "HOME_APPLIANCES",
        "homeAppliances": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "ratedVoltage": "string",
            "powerConsumption": "string",
            "energyEfficiencyRating": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "size": "string",
            "additionalCost": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    SEASON_APPLIANCES = {
        "productInfoProvidedNoticeType": "SEASON_APPLIANCES",
        "seasonAppliances": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "ratedVoltage": "string",
            "powerConsumption": "string",
            "energyEfficiencyRating": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "size": "string",
            "area": "string",
            "installedCharge": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    OFFICE_APPLIANCES = {
        "productInfoProvidedNoticeType": "OFFICE_APPLIANCES",
        "officeAppliances": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "ratedVoltage": "string",
            "powerConsumption": "string",
            "energyEfficiencyRating": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "size": "string",
            "weight": "string",
            "specification": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    OPTICS_APPLIANCES = {
        "productInfoProvidedNoticeType": "OPTICS_APPLIANCES",
        "opticsAppliances": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "size": "string",
            "weight": "string",
            "specification": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    MICROELECTRONICS = {
        "productInfoProvidedNoticeType": "MICROELECTRONICS",
        "microElectronics": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "ratedVoltage": "string",
            "powerConsumption": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "size": "string",
            "weight": "string",
            "specification": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    NAVIGATION = {
        "productInfoProvidedNoticeType": "NAVIGATION",
        "navigation": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "ratedVoltage": "string",
            "powerConsumption": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "size": "string",
            "weight": "string",
            "specification": "string",
            "updateCost": "string",
            "freeCostPeriod": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    CAR_ARTICLES = {
        "productInfoProvidedNoticeType": "CAR_ARTICLES",
        "carArticles": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "certificationType": "string",
            "caution": "string",
            "manufacturer": "string",
            "size": "string",
            "applyModel": "string",
            "warrantyPolicy": "string",
            "roadWorthyCertification": "string",
            "afterServiceDirector": "string",
        },
    }

    MEDICAL_APPLIANCES = {
        "productInfoProvidedNoticeType": "MEDICAL_APPLIANCES",
        "medicalAppliances": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "licenceNo": "string",
            "advertisingCertificationType": "string",
            "ratedVoltage": "string",
            "powerConsumption": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "purpose": "string",
            "usage": "string",
            "caution": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    KITCHEN_UTENSILS = {
        "productInfoProvidedNoticeType": "KITCHEN_UTENSILS",
        "kitchenUtensils": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "material": "string",
            "component": "string",
            "size": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "producer": "string",
            "importDeclaration": True,
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    COSMETIC = {
        "productInfoProvidedNoticeType": "COSMETIC",
        "cosmetic": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "capacity": "string",
            "specification": "string",
            "expirationDate": "string",
            "expirationDateText": "string",
            "usage": "string",
            "manufacturer": "string",
            "producer": "string",
            "distributor": "string",
            "customizedDistributor": "string",
            "mainIngredient": "string",
            "certificationType": "string",
            "caution": "string",
            "warrantyPolicy": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    JEWELLERY = {
        "productInfoProvidedNoticeType": "JEWELLERY",
        "jewellery": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "material": "string",
            "purity": "string",
            "bandMaterial": "string",
            "weight": "string",
            "manufacturer": "string",
            "producer": "string",
            "size": "string",
            "caution": "string",
            "specification": "string",
            "provideWarranty": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    FOOD = {
        "productInfoProvidedNoticeType": "FOOD",
        "food": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "foodItem": "string",
            "weight": "string",
            "amount": "string",
            "size": "string",
            "packDate": "2023-01-30",
            "packDateText": "string",
            "expirationDate": "2023-01-30",
            "expirationDateText": "string",
            "consumptionDate": "2023-01-30",
            "consumptionDateText": "string",
            "producer": "string",
            "relevantLawContent": "string",
            "productComposition": "string",
            "keep": "string",
            "adCaution": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    GENERAL_FOOD = {
        "productInfoProvidedNoticeType": "GENERAL_FOOD",
        "generalFood": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "productName": "string",
            "foodType": "string",
            "producer": "string",
            "location": "string",
            "packDate": "2023-01-30",
            "packDateText": "string",
            "expirationDate": "2023-01-30",
            "expirationDateText": "string",
            "consumptionDate": "2023-01-30",
            "consumptionDateText": "string",
            "weight": "string",
            "amount": "string",
            "ingredients": "string",
            "nutritionFacts": "string",
            "geneticallyModified": True,
            "consumerSafetyCaution": "string",
            "importDeclarationCheck": True,
            "customerServicePhoneNumber": "string",
        },
    }

    DIET_FOOD = {
        "productInfoProvidedNoticeType": "DIET_FOOD",
        "dietFood": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "productName": "string",
            "producer": "string",
            "location": "string",
            "expirationDate": "2023-01-30",
            "expirationDateText": "string",
            "consumptionDate": "2023-01-30",
            "consumptionDateText": "string",
            "storageMethod": "string",
            "weight": "string",
            "amount": "string",
            "ingredients": "string",
            "nutritionFacts": "string",
            "specification": "string",
            "cautionAndSideEffect": "string",
            "nonMedicinalUsesMessage": "string",
            "geneticallyModified": True,
            "importDeclarationCheck": True,
            "consumerSafetyCaution": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    KIDS = {
        "productInfoProvidedNoticeType": "KIDS",
        "kids": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "size": "string",
            "weight": "string",
            "color": "string",
            "material": "string",
            "recommendedAge": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "caution": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
            "numberLimit": "string",
        },
    }

    MUSICAL_INSTRUMENT = {
        "productInfoProvidedNoticeType": "MUSICAL_INSTRUMENT",
        "musicalInstrument": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "size": "string",
            "color": "string",
            "material": "string",
            "components": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "detailContent": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    SPORTS_EQUIPMENT = {
        "productInfoProvidedNoticeType": "SPORTS_EQUIPMENT",
        "sportsEquipment": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "size": "string",
            "weight": "string",
            "color": "string",
            "material": "string",
            "components": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "detailContent": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    BOOKS = {
        "productInfoProvidedNoticeType": "BOOKS",
        "books": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "title": "string",
            "author": "string",
            "publisher": "string",
            "size": "string",
            "pages": "string",
            "components": "string",
            "publishDate": "2023-01-30",
            "publishDateText": "string",
            "description": "string",
        },
    }

    RENTAL_ETC = {
        "productInfoProvidedNoticeType": "RENTAL_ETC",
        "rentalEtc": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "ownershipTransferCondition": "string",
            "payingForLossOrDamage": "string",
            "refundPolicyForCancel": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    DIGITAL_CONTENTS = {
        "productInfoProvidedNoticeType": "DIGITAL_CONTENTS",
        "digitalContents": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "producer": "string",
            "termsOfUse": "string",
            "usePeriod": "string",
            "medium": "string",
            "requirement": "string",
            "cancelationPolicy": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    GIFT_CARD = {
        "productInfoProvidedNoticeType": "GIFT_CARD",
        "giftCard": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "issuer": "string",
            "periodStartDate": "2023-01-30",
            "periodEndDate": "2023-01-30",
            "periodDays": 0,
            "termsOfUse": "string",
            "useStorePlace": "string",
            "useStoreAddressId": 0,
            "useStoreUrl": "string",
            "refundPolicy": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    MOBILE_COUPON = {
        "productInfoProvidedNoticeType": "MOBILE_COUPON",
        "mobileCoupon": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "issuer": "string",
            "usableCondition": "string",
            "usableStore": "string",
            "cancelationPolicy": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    MOVIE_SHOW = {
        "productInfoProvidedNoticeType": "MOVIE_SHOW",
        "movieShow": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "sponsor": "string",
            "actor": "string",
            "rating": "string",
            "showTime": "string",
            "showPlace": "string",
            "cancelationCondition": "string",
            "cancelationPolicy": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    ETC_SERVICE = {
        "productInfoProvidedNoticeType": "ETC_SERVICE",
        "etcService": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "serviceProvider": "string",
            "certificateDetails": "string",
            "usableCondition": "string",
            "cancelationStandard": "string",
            "cancelationPolicy": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    BIOCHEMISTRY = {
        "productInfoProvidedNoticeType": "BIOCHEMISTRY",
        "biochemistry": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "productName": "string",
            "dosageForm": "string",
            "packDate": "string",
            "packDateText": "string",
            "expirationDate": "string",
            "expirationDateText": "string",
            "weight": "string",
            "effect": "string",
            "importer": "string",
            "producer": "string",
            "manufacturer": "string",
            "childProtection": "string",
            "chemicals": "string",
            "caution": "string",
            "safeCriterionNo": "string",
            "customerServicePhoneNumber": "string",
        },
    }

    BIOCIDAL = {
        "productInfoProvidedNoticeType": "BIOCIDAL",
        "biocidal": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "productName": "string",
            "weight": "string",
            "effect": "string",
            "rangeOfUse": "string",
            "importer": "string",
            "producer": "string",
            "manufacturer": "string",
            "childProtection": "string",
            "harmfulChemicalSubstance": "string",
            "maleficence": "string",
            "caution": "string",
            "approvalNumber": "string",
            "customerServicePhoneNumber": "string",
            "expirationDate": "2023-01-30",
            "expirationDateText": "string",
        },
    }

    CELLPHONE = {
        "productInfoProvidedNoticeType": "CELLPHONE",
        "cellPhone": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificationType": "string",
            "releaseDate": "string",
            "releaseDateText": "string",
            "manufacturer": "string",
            "importer": "string",
            "producer": "string",
            "size": "string",
            "weight": "string",
            "telecomType": "string",
            "joinProcess": "string",
            "extraBurden": "string",
            "specification": "string",
            "warrantyPolicy": "string",
            "afterServiceDirector": "string",
        },
    }

    ETC = {
        "productInfoProvidedNoticeType": "ETC",
        "etc": {
            "returnCostReason": "string",
            "noRefundReason": "string",
            "qualityAssuranceStandard": "string",
            "compensationProcedure": "string",
            "troubleShootingContents": "string",
            "itemName": "string",
            "modelName": "string",
            "certificateDetails": "string",
            "manufacturer": "string",
            "afterServiceDirector": "string",
            "customerServicePhoneNumber": "string",
        },
    }
