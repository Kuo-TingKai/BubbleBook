#!/bin/bash
# AUTOMATIC1111 WebUI 批量生成腳本

MODEL="dreamshaper_8.safetensors"
OUTPUT_DIR="/Users/kevin.k/baby_book/illustrations/raw"
STYLE_TAGS="children's book illustration, soft watercolor, gentle colors, pastel colors"

echo "開始生成《泡泡知道自己在哪裡》插圖..."


# 生成 cover
echo "正在生成 cover..."
python scripts/txt2img.py \
    --prompt "A large transparent soap bubble floating in soft sky blue gradient background, rainbow prismatic edges, gentle watercolor illustration style, children's book cover, cute bubble with friendly expression, dreamy atmosphere, soft lighting, pastel colors, 20cm x 20cm square format, $STYLE_TAGS" \
    --negative_prompt "dark, scary, sharp edges, complex details, adult themes" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "cover.png"


# 生成 page_01_birth
echo "正在生成 page_01_birth..."
python scripts/txt2img.py \
    --prompt "Cute cartoon bubble blower machine with smiley face, transparent soap bubble flying out with dotted trail lines, pure white background, gentle watercolor style, children's illustration, soft pastel colors, playful atmosphere, bubble trajectory arrows, friendly cartoon style, $STYLE_TAGS" \
    --negative_prompt "dark background, sharp edges, realistic photography, complex machinery" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_01_birth.png"


# 生成 page_02_mirror
echo "正在生成 page_02_mirror..."
python scripts/txt2img.py \
    --prompt "Transparent soap bubble looking at oval mirror with classical frame, reflection of bubble in mirror with faded colors and dotted border, surprised and happy bubble expressions, round speech bubbles, soft watercolor illustration, gentle lighting, children's book style, $STYLE_TAGS" \
    --negative_prompt "realistic mirror, dark reflections, sharp edges, adult themes" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_02_mirror.png"


# 生成 page_03_world
echo "正在生成 page_03_world..."
python scripts/txt2img.py \
    --prompt "Large transparent soap bubble in center of page, rainbow spectrum flowing inside bubble, flowing wind lines surrounding outside, clear boundary line slightly thickened, soft watercolor style, gentle gradient colors, children's illustration, dreamy atmosphere, $STYLE_TAGS" \
    --negative_prompt "dark colors, sharp boundaries, realistic physics, complex details" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_03_world.png"


# 生成 page_04_expanding
echo "正在生成 page_04_expanding..."
python scripts/txt2img.py \
    --prompt "Expanding soap bubble with multiple bubble contours showing growth process, outward spreading dynamic lines, boundary gradually thinning, tension building effect, deeper colors and dense lines, soft watercolor illustration, children's book style, gentle expansion, $STYLE_TAGS" \
    --negative_prompt "explosive, violent, sharp edges, dark tension, scary expansion" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_04_expanding.png"


# 生成 page_05_burst
echo "正在生成 page_05_burst..."
python scripts/txt2img.py \
    --prompt "Explosive burst effect with colorful rainbow fragments scattering in all directions, spiral wind vortex lines, dynamic tilted composition, soap bubble breaking moment, soft watercolor style, gentle explosion, children's illustration, colorful chaos, $STYLE_TAGS" \
    --negative_prompt "violent explosion, sharp fragments, dark colors, scary elements" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_05_burst.png"


# 生成 page_06_new_bubble
echo "正在生成 page_06_new_bubble..."
python scripts/txt2img.py \
    --prompt "New transparent soap bubble with happy smiley face, bright colors showing new beginning, same design as page 1 but with added smile, gentle watercolor style, children's illustration, hopeful atmosphere, soft lighting, rebirth theme, $STYLE_TAGS" \
    --negative_prompt "dark rebirth, sad expression, sharp edges, complex details" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_06_new_bubble.png"


# 生成 page_07_friends
echo "正在生成 page_07_friends..."
python scripts/txt2img.py \
    --prompt "Group of 3-5 soap bubbles in different sizes, each with unique rainbow colors inside, naturally scattered arrangement maintaining visual balance, each bubble with individual characteristics, soft watercolor style, children's illustration, friendly group scene, $STYLE_TAGS" \
    --negative_prompt "crowded, chaotic arrangement, dark colors, sharp edges, too many bubbles" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_07_friends.png"


# 生成 page_08_hug
echo "正在生成 page_08_hug..."
python scripts/txt2img.py \
    --prompt "Two soap bubbles gently touching with overlapping boundaries, blurred boundary effect using dotted lines and faded colors, heart symbol at contact point, confused questioning expressions on bubbles, soft watercolor style, children's illustration, gentle contact, $STYLE_TAGS" \
    --negative_prompt "violent collision, sharp contact, dark emotions, complex physics" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_08_hug.png"


# 生成 page_09_merge
echo "正在生成 page_09_merge..."
python scripts/txt2img.py \
    --prompt "Two soap bubbles merging into one large bubble with arrow showing transformation, mixed rainbow colors inside large bubble, newly drawn clear boundary, soft watercolor style, children's illustration, gentle fusion process, unity theme, $STYLE_TAGS" \
    --negative_prompt "violent merger, sharp transformation, dark fusion, complex physics" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_09_merge.png"


# 生成 page_10_thinking
echo "正在生成 page_10_thinking..."
python scripts/txt2img.py \
    --prompt "Single soap bubble floating quietly with thinking expression, small thought bubbles surrounding large bubble, calm colors and peaceful composition, contemplative atmosphere, soft watercolor style, children's illustration, philosophical mood, $STYLE_TAGS" \
    --negative_prompt "dark contemplation, sharp thoughts, scary philosophy, complex thinking" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_10_thinking.png"


# 生成 page_11_understanding
echo "正在生成 page_11_understanding..."
python scripts/txt2img.py \
    --prompt "Happy soap bubble with bright smile, artistic brush strokes surrounding bubble showing creativity, bright colors and open composition, enlightenment feeling, soft watercolor style, children's illustration, joyful realization, creative atmosphere, $STYLE_TAGS" \
    --negative_prompt "dark enlightenment, sharp realization, scary creativity, complex art" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_11_understanding.png"


# 生成 page_12_continuing
echo "正在生成 page_12_continuing..."
python scripts/txt2img.py \
    --prompt "Soap bubble flying toward edge of page, infinite gradient sky background extending to infinity, warm colors and complete composition, continuous flying motion, soft watercolor style, children's illustration, eternal journey theme, $STYLE_TAGS" \
    --negative_prompt "dark journey, sharp flying, scary infinity, complex travel" \
    --width 1024 \
    --height 1024 \
    --steps 50 \
    --cfg_scale 7.5 \
    --sampler_name euler_a \
    --batch_size 1 \
    --output_dir "$OUTPUT_DIR" \
    --filename "page_12_continuing.png"


echo "所有插圖生成完成！"
echo "請檢查 $OUTPUT_DIR 目錄中的結果"
