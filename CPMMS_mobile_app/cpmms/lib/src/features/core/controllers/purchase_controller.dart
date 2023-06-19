import 'package:get/get.dart';
import 'package:cpmms/src/features/core/models/purchase_model.dart';
import 'package:cpmms/src/repository/purchase_repository/purchase_repository.dart';

class TrackPurchaseController extends GetxController {
  static TrackPurchaseController get instance => Get.find();

  final _purchaseRepo = Get.put(TrackPurchaseRepository());
  final RxBool isLoading = true.obs;
  final RxList<PurchaseModel> purchaseHistoryData = RxList<PurchaseModel>();

  Future<void> getPurchaseHistory(String memID) async{
    final data = await _purchaseRepo.getPurchase(memID);
    purchaseHistoryData.value = data;
    isLoading.value = false;
  }
}
