// openailabfaceapi.h
//初始化模块
// Parameters:
//   log_path -- the log file path
// return:
//   0 -- for OK
//   < 0 -- for error
int initial(char* log_path);
//结束模块
// return:
//   0 -- for OK
//   < 0 -- for error
int deinitial();
//人脸照片有效性判断，单张照片中是否可以检测到有效的人脸；
// Parameters:
//  jpegFileName – 相片
// Return:
//  图片里脸所在的位置，左、上、宽、高
struct FaceRect{
    int left;
    int top;
    int width;
    int height;
};
struct FaceRect FaceExisted(char* jpegFileName); //出错时， width == 0
//人脸照片的质量判断，人脸照片质量是否影响其作为最优注册人脸照片（对识别所需的特征无损）；
// Parameters:
//  jpegFileName – 相片
//  rectangle – 矩形框FaceInfor
//  threshold – 阀值（0~1，-1即使用系统缺省值）（评分高于此值的为合规照片）
// Return:
//  0 for OK (图像质量符合条件)
//  others for not good
//    1 --  图像不清晰
//    2 --  角度不合理
//    3 --  超过最大左转角度
//    4 --  超过最大右转角度
//    5 --  超过最大上仰角度
//    6 --  超过最大俯视角度
//    7 --  超过最大水平旋转角度
//    8 --  没有检测到人脸
int FaceQualityOK(char* jpegFileName, struct FaceRect rectangle, float threshold); 
//同一用户多张照片（3~5张）的有效性判断，确定多张照片是否为同一人；
// Parameters:
//   jpegFileNameList – 为多张图片
//   threshold – 阀值（0~1，-1即使用系统缺省值）
// Return:
//   1 为同一个人
//   0 为不同人
int FaceIsSamePerson(char** jpegFileNameList, float threshold); 
//同一用户多张照片（3~5张）里的最佳照片；
// Parameters:
//  jpegFileNameList – 为多张图片（n张照片）
// Return:
//  index（第几张图为最佳照片，0~n-1）
int BestFacePicture(char** jpegFileNameList, float threshold); 

