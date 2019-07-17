from stagesepx.cutter import VideoCutter


# 改为你的视频路径
video_path = '../test.mp4'

cutter = VideoCutter(
    # 步长，默认为2，通过它可以自行把握效率与颗粒度
    # 设定为2时，会以2帧为一个单位进行遍历
    period=2,
    # 默认为0.2，即将图片缩放为0.2倍
    # 主要为了提高计算效率
    compress_rate=0.2
)

# 开始切割
res = cutter.cut(video_path)

# 你可以通过res获取切割结果
# 例如稳定状态对应的区间
# limit能够过滤掉一些过于短的阶段（例如你不希望一些持续时间过短的阶段被认为是一个稳态），默认不过滤
stable = res.get_stable_range()
# 不稳定状态（正在变化）
unstable = res.get_unstable_range()

# 对区间进行采样
data_path = res.pick_and_save(
    # 这里的例子是对稳定区间进行采样
    stable,
    # 每段区间的采样数，3即每个阶段等距离截取3张图片
    3,
    # 采样结果保存的位置
    # 不指定的话则会在当前位置生成文件夹并返回它的路径
    './cut_result',
)
print(f'data saved to {data_path}')
