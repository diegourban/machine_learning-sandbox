package urban;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.Recommender;

import java.io.IOException;
import java.util.List;

public class CourseRecommender {

    public static void main(String[] args) throws IOException, TasteException {
        DataModel coursesDataModel = new RecommenderDataModel().getCoursesModel();
        Recommender recommender = new MyRecommenderBuilder().buildRecommender(coursesDataModel);

        int userId = 1;
        int totalRecommendations = 3;

        List<RecommendedItem> recommendations = recommender.recommend(userId, totalRecommendations);
        for (RecommendedItem recommendedItem : recommendations) {
            System.out.println(recommendedItem);
        }

    }
}
