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
            # "packDate": "yyyy-MM",
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
            "returnCostReason": "0",  # 미입력 시 상품상세 참조
            "noRefundReason": "0",  # 미입력 시 상품상세 참조
            "qualityAssuranceStandard": "0",  # 미입력 시 상품상세 참조
            "compensationProcedure": "0",  # 미입력 시 상품상세 참조
            "troubleShootingContents": "0",  # 미입력 시 상품상세 참조
            "material": "상품상세참조",
            "color": "상품상세참조",
            "size": "상품상세참조",
            "components": "상품상세참조",
            "manufacturer": "상품상세참조",
            "caution": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    FURNITURE = {
        "productInfoProvidedNoticeType": "FURNITURE",
        "furniture": {
            "returnCostReason": "0",  # 미입력 시 상품상세 참조
            "noRefundReason": "0",  # 미입력 시 상품상세 참조
            "qualityAssuranceStandard": "0",  # 미입력 시 상품상세 참조
            "compensationProcedure": "0",  # 미입력 시 상품상세 참조
            "troubleShootingContents": "0",  # 미입력 시 상품상세 참조
            "itemName": "상품상세참조",
            "certificationType": "상품상세참조",
            "color": "상품상세참조",
            "components": "상품상세참조",
            "material": "상품상세참조",
            "manufacturer": "상품상세참조",
            "importer": "상품상세참조",
            "producer": "상품상세참조",
            "size": "상품상세참조",
            "installedCharge": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "refurb": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    IMAGE_APPLIANCES = {
        "productInfoProvidedNoticeType": "IMAGE_APPLIANCES",
        "imageAppliances": {
            "returnCostReason": "0",  # 미입력 시 상품상세 참조
            "noRefundReason": "0",  # 미입력 시 상품상세 참조
            "qualityAssuranceStandard": "0",  # 미입력 시 상품상세 참조
            "compensationProcedure": "0",  # 미입력 시 상품상세 참조
            "troubleShootingContents": "0",  # 미입력 시 상품상세 참조
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            "ratedVoltage": "상품상세참조",
            "powerConsumption": "상품상세참조",
            "energyEfficiencyRating": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "size": "상품상세참조",
            "additionalCost": "상품상세참조",
            "displaySpecification": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    HOME_APPLIANCES = {
        "productInfoProvidedNoticeType": "HOME_APPLIANCES",
        "homeAppliances": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            "ratedVoltage": "상품상세참조",
            "powerConsumption": "상품상세참조",
            "energyEfficiencyRating": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "size": "상품상세참조",
            "additionalCost": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    SEASON_APPLIANCES = {
        "productInfoProvidedNoticeType": "SEASON_APPLIANCES",
        "seasonAppliances": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            "ratedVoltage": "상품상세참조",
            "powerConsumption": "상품상세참조",
            "energyEfficiencyRating": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "size": "상품상세참조",
            "area": "상품상세참조",
            "installedCharge": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    OFFICE_APPLIANCES = {
        "productInfoProvidedNoticeType": "OFFICE_APPLIANCES",
        "officeAppliances": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            "ratedVoltage": "상품상세참조",
            "powerConsumption": "상품상세참조",
            "energyEfficiencyRating": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "size": "상품상세참조",
            "weight": "상품상세참조",
            "specification": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    OPTICS_APPLIANCES = {
        "productInfoProvidedNoticeType": "OPTICS_APPLIANCES",
        "opticsAppliances": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "size": "상품상세참조",
            "weight": "상품상세참조",
            "specification": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    MICROELECTRONICS = {
        "productInfoProvidedNoticeType": "MICROELECTRONICS",
        "microElectronics": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            "ratedVoltage": "상품상세참조",
            "powerConsumption": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "size": "상품상세참조",
            "weight": "상품상세참조",
            "specification": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    NAVIGATION = {
        "productInfoProvidedNoticeType": "NAVIGATION",
        "navigation": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            "ratedVoltage": "상품상세참조",
            "powerConsumption": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "size": "상품상세참조",
            "weight": "상품상세참조",
            "specification": "상품상세참조",
            "updateCost": "상품상세참조",
            "freeCostPeriod": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    CAR_ARTICLES = {
        "productInfoProvidedNoticeType": "CAR_ARTICLES",
        "carArticles": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "certificationType": "상품상세참조",
            "caution": "상품상세참조",
            "manufacturer": "상품상세참조",
            "size": "상품상세참조",
            "applyModel": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "roadWorthyCertification": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    MEDICAL_APPLIANCES = {
        "productInfoProvidedNoticeType": "MEDICAL_APPLIANCES",
        "medicalAppliances": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "licenceNo": "상품상세참조",
            "advertisingCertificationType": "상품상세참조",
            "ratedVoltage": "상품상세참조",
            "powerConsumption": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "purpose": "상품상세참조",
            "usage": "상품상세참조",
            "caution": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    KITCHEN_UTENSILS = {
        "productInfoProvidedNoticeType": "KITCHEN_UTENSILS",
        "kitchenUtensils": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "material": "상품상세참조",
            "component": "상품상세참조",
            "size": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "producer": "상품상세참조",
            # "importDeclaration": "false",  # 수입식품안전관리특별법에 따른 수입신고 (미 입력시 false)
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    COSMETIC = {
        "productInfoProvidedNoticeType": "COSMETIC",
        "cosmetic": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "capacity": "상품상세참조",
            "specification": "상품상세참조",
            # "expirationDate": "yyyy-MM",
            "expirationDateText": "상품상세참조",
            "usage": "상품상세참조",
            "manufacturer": "상품상세참조",
            "producer": "상품상세참조",
            "distributor": "상품상세참조",
            "customizedDistributor": "상품상세참조",
            "mainIngredient": "상품상세참조",
            "certificationType": "상품상세참조",
            "caution": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    JEWELLERY = {
        "productInfoProvidedNoticeType": "JEWELLERY",
        "jewellery": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "material": "상품상세참조",
            "purity": "상품상세참조",
            "bandMaterial": "상품상세참조",
            "weight": "상품상세참조",
            "manufacturer": "상품상세참조",
            "producer": "상품상세참조",
            "size": "상품상세참조",
            "caution": "상품상세참조",
            "specification": "상품상세참조",
            "provideWarranty": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    FOOD = {
        "productInfoProvidedNoticeType": "FOOD",
        "food": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "foodItem": "상품상세참조",
            "weight": "상품상세참조",
            "amount": "상품상세참조",
            "size": "상품상세참조",
            # "packDate": "2023-01-30",
            "packDateText": "상품상세참조",
            # "expirationDate": "2023-01-30", # 유통기한 -> 삭제예정
            "expirationDateText": "상품상세참조",
            # "consumptionDate": "2023-01-30",
            "consumptionDateText": "상품상세참조",
            "producer": "상품상세참조",
            "relevantLawContent": "상품상세참조",
            "productComposition": "상품상세참조",
            "keep": "상품상세참조",
            "adCaution": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    GENERAL_FOOD = {
        "productInfoProvidedNoticeType": "GENERAL_FOOD",
        "generalFood": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "productName": "상품상세참조",
            "foodType": "상품상세참조",
            "producer": "상품상세참조",
            "location": "상품상세참조",
            # "packDate": "2023-01-30",
            "packDateText": "상품상세참조",
            # "expirationDate": "2023-01-30", # 유통기한 -> 삭제예정
            "expirationDateText": "상품상세참조",
            # "consumptionDate": "2023-01-30",
            "consumptionDateText": "상품상세참조",
            "weight": "상품상세참조",
            "amount": "상품상세참조",
            "ingredients": "상품상세참조",
            "nutritionFacts": "상품상세참조",
            "geneticallyModified": "false",  # 유전자변형식품에 해당하는 경우의 표시
            "consumerSafetyCaution": "상품상세참조",
            "importDeclarationCheck": "false",  # 수입식품의 경우 신고 필 유무
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    DIET_FOOD = {
        "productInfoProvidedNoticeType": "DIET_FOOD",
        "dietFood": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "productName": "상품상세참조",
            "producer": "상품상세참조",
            "location": "상품상세참조",
            # "expirationDate": "2023-01-30", # 유통기한 -> 삭제예정
            "expirationDateText": "상품상세참조",
            # "consumptionDate": "2023-01-30",
            "consumptionDateText": "상품상세참조",
            "storageMethod": "상품상세참조",
            "weight": "상품상세참조",
            "amount": "상품상세참조",
            "ingredients": "상품상세참조",
            "nutritionFacts": "상품상세참조",
            "specification": "상품상세참조",
            "cautionAndSideEffect": "상품상세참조",
            "nonMedicinalUsesMessage": "상품상세참조",
            "geneticallyModified": "false",  # 유전자변형식품에 해당하는 경우의 표시
            "importDeclarationCheck": "false",  # 수입식품의 경우 신고 필 유무
            "consumerSafetyCaution": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    KIDS = {
        "productInfoProvidedNoticeType": "KIDS",
        "kids": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            "size": "상품상세참조",
            "weight": "상품상세참조",
            "color": "상품상세참조",
            "material": "상품상세참조",
            "recommendedAge": "상품상세참조",
            "releaseDate": "상품상세참조",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "caution": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
            "numberLimit": "상품상세참조",
        },
    }

    MUSICAL_INSTRUMENT = {
        "productInfoProvidedNoticeType": "MUSICAL_INSTRUMENT",
        "musicalInstrument": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "size": "상품상세참조",
            "color": "상품상세참조",
            "material": "상품상세참조",
            "components": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "detailContent": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    SPORTS_EQUIPMENT = {
        "productInfoProvidedNoticeType": "SPORTS_EQUIPMENT",
        "sportsEquipment": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            "size": "상품상세참조",
            "weight": "상품상세참조",
            "color": "상품상세참조",
            "material": "상품상세참조",
            "components": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "detailContent": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    BOOKS = {
        "productInfoProvidedNoticeType": "BOOKS",
        "books": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "title": "상품상세참조",
            "author": "상품상세참조",
            "publisher": "상품상세참조",
            "size": "상품상세참조",
            "pages": "상품상세참조",
            "components": "상품상세참조",
            # "publishDate": "2023-01-30",
            "publishDateText": "상품상세참조",
            "description": "상품상세참조",
        },
    }

    RENTAL_ETC = {
        "productInfoProvidedNoticeType": "RENTAL_ETC",
        "rentalEtc": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "ownershipTransferCondition": "상품상세참조",
            "payingForLossOrDamage": "상품상세참조",
            "refundPolicyForCancel": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    DIGITAL_CONTENTS = {
        "productInfoProvidedNoticeType": "DIGITAL_CONTENTS",
        "digitalContents": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "producer": "상품상세참조",
            "termsOfUse": "상품상세참조",
            "usePeriod": "상품상세참조",
            "medium": "상품상세참조",
            "requirement": "상품상세참조",
            "cancelationPolicy": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    GIFT_CARD = {
        "productInfoProvidedNoticeType": "GIFT_CARD",
        "giftCard": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "issuer": "상품상세참조",
            # "periodStartDate": "2023-01-30",
            # "periodEndDate": "2023-01-30",
            "periodDays": 0,  # 유효기간 (구매일로부터 00일)
            "termsOfUse": "상품상세참조",
            "useStorePlace": "상품상세참조",  # useStorePlace, useStoreAddressId, useStoreUrl 셋 중 하나 필수 # 기본값은 장소 -> 상세정보참조
            # "useStoreAddressId": 0,
            # "useStoreUrl": "상품상세참조",
            "refundPolicy": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    MOBILE_COUPON = {
        "productInfoProvidedNoticeType": "MOBILE_COUPON",
        "mobileCoupon": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "issuer": "상품상세참조",
            "usableCondition": "상품상세참조",
            "usableStore": "상품상세참조",
            "cancelationPolicy": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    MOVIE_SHOW = {
        "productInfoProvidedNoticeType": "MOVIE_SHOW",
        "movieShow": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "sponsor": "상품상세참조",
            "actor": "상품상세참조",
            "rating": "상품상세참조",
            "showTime": "상품상세참조",
            "showPlace": "상품상세참조",
            "cancelationCondition": "상품상세참조",
            "cancelationPolicy": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    ETC_SERVICE = {
        "productInfoProvidedNoticeType": "ETC_SERVICE",
        "etcService": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "serviceProvider": "상품상세참조",
            "certificateDetails": "상품상세참조",
            "usableCondition": "상품상세참조",
            "cancelationStandard": "상품상세참조",
            "cancelationPolicy": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    BIOCHEMISTRY = {
        "productInfoProvidedNoticeType": "BIOCHEMISTRY",
        "biochemistry": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "productName": "상품상세참조",
            "dosageForm": "상품상세참조",
            # "packDate": "yyyy-MM",
            "packDateText": "상품상세참조",
            # "expirationDate": "yyyy-MM",
            "expirationDateText": "상품상세참조",
            "weight": "상품상세참조",
            "effect": "상품상세참조",
            "importer": "상품상세참조",
            "producer": "상품상세참조",
            "manufacturer": "상품상세참조",
            "childProtection": "상품상세참조",
            "chemicals": "상품상세참조",
            "caution": "상품상세참조",
            "safeCriterionNo": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }

    BIOCIDAL = {
        "productInfoProvidedNoticeType": "BIOCIDAL",
        "biocidal": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "productName": "상품상세참조",
            "weight": "상품상세참조",
            "effect": "상품상세참조",
            "rangeOfUse": "상품상세참조",
            "importer": "상품상세참조",
            "producer": "상품상세참조",
            "manufacturer": "상품상세참조",
            "childProtection": "상품상세참조",
            "harmfulChemicalSubstance": "상품상세참조",
            "maleficence": "상품상세참조",
            "caution": "상품상세참조",
            "approvalNumber": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
            # "expirationDate": "2023-01-30",
            "expirationDateText": "상품상세참조",
        },
    }

    CELLPHONE = {
        "productInfoProvidedNoticeType": "CELLPHONE",
        "cellPhone": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificationType": "상품상세참조",
            # "releaseDate": "yyyy-MM",
            "releaseDateText": "상품상세참조",
            "manufacturer": "상품상세참조",
            "importer": "상품상세참조",
            "producer": "상품상세참조",
            "size": "상품상세참조",
            "weight": "상품상세참조",
            "telecomType": "상품상세참조",
            "joinProcess": "상품상세참조",
            "extraBurden": "상품상세참조",
            "specification": "상품상세참조",
            "warrantyPolicy": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
        },
    }

    ETC = {
        "productInfoProvidedNoticeType": "ETC",
        "etc": {
            "returnCostReason": "0",
            "noRefundReason": "0",
            "qualityAssuranceStandard": "0",
            "compensationProcedure": "0",
            "troubleShootingContents": "0",
            "itemName": "상품상세참조",
            "modelName": "상품상세참조",
            "certificateDetails": "상품상세참조",
            "manufacturer": "상품상세참조",
            "afterServiceDirector": "상품상세참조",
            "customerServicePhoneNumber": "상품상세참조",
        },
    }
