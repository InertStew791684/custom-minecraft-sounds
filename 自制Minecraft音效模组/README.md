# 自制 Minecraft 音效（Fabric 1.21.1）

这是一个纯客户端、无需 Fabric API 的 Fabric 音效模组。它把 `自制Minecraft音效` 目录中的 30 个 MP3 裁掉首尾静音、转为单声道 OGG Vorbis，并完整替换对应的 Minecraft 1.21.1 原版音效事件。

## 安装

1. 安装 Minecraft 1.21.1 和 Fabric Loader 0.16.0 或更高版本。
2. 将 `build/libs/custom-minecraft-sounds-1.21.1-fabric-1.0.0.jar` 放进 Minecraft 的 `mods` 文件夹。
3. 启动游戏。这个模组只需要装在客户端，不需要 Fabric API。

## 映射摘要

- `PlaceBlock.mp3`：覆盖 Minecraft 1.21.1 的全部 107 个 `block.*.place` 方块放置事件。
- `Sand.mp3`：普通沙子和可疑的沙子的破坏、下落、击打、踩踏事件；放置仍使用 `PlaceBlock.mp3`。
- `Villager.mp3`、`pig.mp3`、`cat.mp3`、`Wolf.mp3`、`zombie.mp3`、`Sheep.mp3`、`Spider.mp3`：完整覆盖对应生物的全部 `entity.<生物>.*` 事件，包括环境、受伤、死亡、脚步及该生物的其他行为；不会再播放这些生物的任何原版音效。
- `Villager-Hurt.mp3`：在村民的完整覆盖中单独用于受伤事件；`Steve-Hurt.mp3`：玩家的普通、溺水、冰冻、着火和甜浆果丛受伤。
- `Drinking.mp3`、`Eating.mp3`：通用饮用和进食。
- `fall-down.mp3`：玩家、敌对生物及通用实体的大小跌落落地声。
- `Fall-in-water.mp3`：玩家、敌对生物及通用实体入水声。
- `firework.mp3`：烟花发射；`TNTExplosion:FireworkExplosion.mp3`：TNT 点燃、TNT/通用爆炸及全部远近烟花爆炸。烟花爆炸使用 256 格衰减距离并预加载，避免高空或远处无声。
- `Anvil-Fall.mp3`：铁砧下落及落地。
- `Open-chest.mp3`、`Close-chest.mp3`：普通箱子与末影箱的打开、关闭事件；陷阱箱沿用普通箱子的事件，因此也会被替换。
- `Bell.mp3`：村庄钟的敲击与共鸣事件。
- `Cow.mp3`：完整覆盖牛的全部实体事件。
- `Drown.mp3`：玩家溺水受伤，优先于通用的 `Steve-Hurt.mp3`。
- `Raining.mp3`：露天和有方块遮挡时的雨声。
- `Bee.mp3`：完整覆盖蜜蜂的全部实体事件。
- `Chicken.mp3`：完整覆盖鸡的全部实体事件。
- `zombie.mp3`：除普通僵尸外，同时完整覆盖僵尸村民的环境、转化、治愈、死亡、受伤和脚步事件。
- `Door-Open.mp3`、`Door-Close.mp3`：所有普通门、活板门和栅栏门材质的开启与关闭，包括木、竹、樱花木、下界木、铁和铜类型。
- `Frog.mp3`：完整覆盖青蛙的全部实体事件。
- `Warden.mp3`：完整覆盖监守者的全部实体事件。

所有上述事件都在 `assets/minecraft/sounds.json` 中使用 `"replace": true`，因此不会保留或随机播放对应的原版声音。

## 重新处理音频

如需替换原始 MP3 后重新生成资源：

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-audio.txt
python3 tools/process_audio.py
./gradlew build
```

脚本使用 10 毫秒窗口和 -50 dBFS 阈值裁剪首尾无声段，并分别保留 50 毫秒前沿和 80 毫秒尾沿，避免切掉发音起止。项目内当前生成的 `sounds.json` 还保留了原版字幕键。
