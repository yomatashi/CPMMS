import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:cpmms/src/features/authentications/models/promotion_model.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:firebase_storage/firebase_storage.dart' as firebase_storage;

class PromotionRepository extends GetxController {
  static PromotionRepository get instance => Get.find();

  final _db = FirebaseFirestore.instance;

  Future<List<PromotionModel>> getPromotionList() async {
    final snapshot = await _db.collection("Promotion").get();
    final promotionData =
        snapshot.docs.map((e) => PromotionModel.fromSnapshot(e)).toList();
    return promotionData;
  }

  Future<PromotionModel> getPromotionDetails(String promoID) async {
    final snapshot = await _db
        .collection("Promotion")
        .where(FieldPath.documentId, isEqualTo: promoID)
        .get();
    final promoData =
        snapshot.docs.map((e) => PromotionModel.fromSnapshot(e)).single;
    return promoData;
  }

  createPromotion(PromotionModel promo) async {
    promo.id = await _db
        .collection("Promotion")
        .add(promo.toJson())
        .whenComplete(
          () => Get.snackbar("Success", "New promotion has been added",
              snackPosition: SnackPosition.BOTTOM,
              backgroundColor: Colors.green,
              colorText: Colors.white),
        )
        .then((doc) => doc.id)
        .catchError(
      (error, StackTrace) {
        Get.snackbar("Error", "Something went wrong. Try again",
            snackPosition: SnackPosition.BOTTOM,
            backgroundColor: Colors.redAccent,
            colorText: Colors.white);
      },
    );
    promo.img = "promotion/${promo.id}.jpg";

    await _db
        .collection("Promotion")
        .doc(promo.id)
        .update({"img": 'promotion/${promo.id}.jpg'});
  }

  Future<void> updatePromotion(PromotionModel promo) async {
    await _db.collection("Promotion").doc(promo.id).update(promo.toJson());
  }

  Future<void> deletePromotion(PromotionModel promo) async {
    final storageRef = firebase_storage.FirebaseStorage.instance.ref();
    // Check if the path exists
    final exists = await storageRef
        .child(promo.img)
        .getMetadata()
        .then((metadata) => true)
        .catchError((error) => false);

    if (exists) {
      // Delete the file at the specified path
      await storageRef.child(promo.img).delete();
    } else {}

    await _db.collection("Promotion").doc(promo.id).delete().whenComplete(
          () => Get.snackbar("Success", "Successfully deleted!",
              snackPosition: SnackPosition.BOTTOM,
              backgroundColor: Colors.green,
              colorText: Colors.white),
        );
  }
}
