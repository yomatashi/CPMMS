import 'package:get/get.dart';
import 'package:cpmms/src/features/core/models/purchase_model.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class TrackPurchaseRepository extends GetxController {
  static TrackPurchaseRepository get instance => Get.find();
  final _db = FirebaseFirestore.instance;

Future<List<PurchaseModel>> getPurchase(String memID) async {
    final snapshot = await _db.collection("purchaseHistory").where("memberID", isEqualTo: memID).orderBy("date", descending: true).get();
    final promotionData =
        snapshot.docs.map((e) => PurchaseModel.fromSnapshot(e)).toList();
    return promotionData;
  }
}
