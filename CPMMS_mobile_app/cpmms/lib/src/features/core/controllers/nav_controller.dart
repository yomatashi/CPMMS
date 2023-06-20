import 'package:cpmms/src/features/core/screens/dashboard/dashboard.dart';
import 'package:cpmms/src/features/core/screens/dashboard/dashboard_admin.dart';
import 'package:cpmms/src/features/core/screens/dashboard/dashboard_guest.dart';
import 'package:cpmms/src/features/core/screens/member_points/member_points.dart';
import 'package:cpmms/src/features/core/screens/payment/payment.dart';
import 'package:cpmms/src/features/core/screens/promotion/promotion_admin.dart';
import 'package:cpmms/src/features/core/screens/purchase_history/purchase_history.dart';
import 'package:cpmms/src/features/core/screens/rewards/rewards.dart';
import 'package:cpmms/src/features/core/screens/rewards/rewards_admin.dart';
import 'package:get/get.dart';

class NavigationController extends GetxController {
  static NavigationController get to => Get.find();
  var selectedIndex = 0.obs;

  void changePage(int index) {
    selectedIndex.value = index;
    switch (index) {
      case 0:
        Get.off(const Dashboard(), transition: Transition.fadeIn);
        break;
      case 1:
        Get.off(const MemberPoints(), transition: Transition.fadeIn);
        break;
      case 2:
        Get.off(const Rewards(), transition: Transition.fadeIn);
        break;
      case 3:
        Get.off(const PurchaseHistory(), transition: Transition.fadeIn);
        break;
      case 4:
        Get.off(const Payment(), transition: Transition.fadeIn);
        break;
    }
  }

  void changePageAdmin(int index) {
    selectedIndex.value = index;
    switch (index) {
      case 0:
        Get.off(const DashboardAdmin(), transition: Transition.fadeIn);
        break;
      case 1:
        Get.off(const RewardsManager(), transition: Transition.fadeIn);
        break;
      case 2:
        Get.off(const PromotionManager(), transition: Transition.fadeIn);
        break;
    }
  }

  void changePageGuest(int index) {
    selectedIndex.value = index;
    switch (index) {
      case 0:
        Get.off(const DashboardGuest(), transition: Transition.fadeIn);
        break;
    }
  }
}
