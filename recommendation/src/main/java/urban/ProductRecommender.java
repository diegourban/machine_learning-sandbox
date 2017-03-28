package urban;

import java.io.IOException;
import java.util.List;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.Recommender;

public class ProductRecommender {

    public static void main(String[] args) throws IOException, TasteException {
        DataModel productsModel = new RecommenderDataModel().getProductsModel();
        Recommender recommender = new MyRecommenderBuilder().buildRecommender(productsModel);

        printRecommendationsForUser(recommender, 1, 4);
        printRecommendationsForUser(recommender, 3, 4);
        printRecommendationsForUser(recommender, 4, 4);
    }

    private static void printRecommendationsForUser(Recommender recommender, int userId, int totalRecommendations) throws TasteException {
        System.out.println("User " + userId);
        List<RecommendedItem> recommendations = recommender.recommend(userId, totalRecommendations);
        for (RecommendedItem recommendedItem : recommendations) {
            System.out.println(recommendedItem);
        }
    }

}
