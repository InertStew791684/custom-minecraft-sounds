#!/usr/bin/env python3
"""Trim the supplied MP3 files, convert them to mono OGG Vorbis, and build sounds.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


MOD_ID = "custom_minecraft_sounds"
PROJECT_DIR = Path(__file__).resolve().parent.parent

AUDIO_FILES = {
    "Anvil-Fall.mp3": "anvil_fall",
    "Bee.mp3": "bee",
    "Bell.mp3": "bell",
    "Chicken.mp3": "chicken",
    "Close-chest.mp3": "close_chest",
    "Cow.mp3": "cow",
    "Door-Close.mp3": "door_close",
    "Door-Open.mp3": "door_open",
    "Drinking.mp3": "drinking",
    "Drown.mp3": "drown",
    "Eating.mp3": "eating",
    "Fall-in-water.mp3": "fall_in_water",
    "Frog.mp3": "frog",
    "Open-chest.mp3": "open_chest",
    "PlaceBlock.mp3": "place_block",
    "Raining.mp3": "raining",
    "Sand.mp3": "sand",
    "Sheep.mp3": "sheep",
    "Spider.mp3": "spider",
    "Steve-Hurt.mp3": "steve_hurt",
    "TNTExplosion:FireworkExplosion.mp3": "explosion",
    "Villager-Hurt.mp3": "villager_hurt",
    "Villager.mp3": "villager",
    "Warden.mp3": "warden",
    "Wolf.mp3": "wolf",
    "cat.mp3": "cat",
    "fall-down.mp3": "fall_down",
    "firework.mp3": "firework",
    "pig.mp3": "pig",
    "zombie.mp3": "zombie",
}

EVENT_GROUPS = {
    "anvil_fall": ["block.anvil.fall", "block.anvil.land"],
    "bee": [
        "entity.bee.death",
        "entity.bee.hurt",
        "entity.bee.loop",
        "entity.bee.loop_aggressive",
        "entity.bee.pollinate",
        "entity.bee.sting",
    ],
    "bell": ["block.bell.resonate", "block.bell.use"],
    "chicken": [
        "entity.chicken.ambient",
        "entity.chicken.death",
        "entity.chicken.egg",
        "entity.chicken.hurt",
        "entity.chicken.step",
    ],
    "close_chest": ["block.chest.close", "block.ender_chest.close"],
    "cow": [
        "entity.cow.ambient",
        "entity.cow.death",
        "entity.cow.hurt",
        "entity.cow.milk",
        "entity.cow.step",
    ],
    "drinking": ["entity.generic.drink"],
    "drown": ["entity.player.hurt_drown"],
    "door_close": [
        "block.bamboo_wood_door.close",
        "block.bamboo_wood_fence_gate.close",
        "block.bamboo_wood_trapdoor.close",
        "block.cherry_wood_door.close",
        "block.cherry_wood_fence_gate.close",
        "block.cherry_wood_trapdoor.close",
        "block.copper_door.close",
        "block.copper_trapdoor.close",
        "block.fence_gate.close",
        "block.iron_door.close",
        "block.iron_trapdoor.close",
        "block.nether_wood_door.close",
        "block.nether_wood_fence_gate.close",
        "block.nether_wood_trapdoor.close",
        "block.wooden_door.close",
        "block.wooden_trapdoor.close",
    ],
    "door_open": [
        "block.bamboo_wood_door.open",
        "block.bamboo_wood_fence_gate.open",
        "block.bamboo_wood_trapdoor.open",
        "block.cherry_wood_door.open",
        "block.cherry_wood_fence_gate.open",
        "block.cherry_wood_trapdoor.open",
        "block.copper_door.open",
        "block.copper_trapdoor.open",
        "block.fence_gate.open",
        "block.iron_door.open",
        "block.iron_trapdoor.open",
        "block.nether_wood_door.open",
        "block.nether_wood_fence_gate.open",
        "block.nether_wood_trapdoor.open",
        "block.wooden_door.open",
        "block.wooden_trapdoor.open",
    ],
    "eating": ["entity.generic.eat"],
    "fall_in_water": [
        "entity.generic.splash",
        "entity.hostile.splash",
        "entity.player.splash",
        "entity.player.splash.high_speed",
    ],
    "sand": [
        "block.sand.break",
        "block.sand.fall",
        "block.sand.hit",
        "block.sand.step",
        "block.suspicious_sand.break",
        "block.suspicious_sand.fall",
        "block.suspicious_sand.hit",
        "block.suspicious_sand.step",
    ],
    "sheep": [
        "entity.sheep.ambient",
        "entity.sheep.death",
        "entity.sheep.hurt",
        "entity.sheep.shear",
        "entity.sheep.step",
    ],
    "spider": [
        "entity.spider.ambient",
        "entity.spider.death",
        "entity.spider.hurt",
        "entity.spider.step",
    ],
    "steve_hurt": [
        "entity.player.hurt",
        "entity.player.hurt_freeze",
        "entity.player.hurt_on_fire",
        "entity.player.hurt_sweet_berry_bush",
    ],
    "explosion": [
        "entity.generic.explode",
        "entity.tnt.primed",
        "entity.firework_rocket.blast",
        "entity.firework_rocket.blast_far",
        "entity.firework_rocket.large_blast",
        "entity.firework_rocket.large_blast_far",
        "entity.firework_rocket.twinkle",
        "entity.firework_rocket.twinkle_far",
    ],
    "villager_hurt": ["entity.villager.hurt"],
    "villager": [
        "entity.villager.ambient",
        "entity.villager.celebrate",
        "entity.villager.death",
        "entity.villager.no",
        "entity.villager.trade",
        "entity.villager.work_armorer",
        "entity.villager.work_butcher",
        "entity.villager.work_cartographer",
        "entity.villager.work_cleric",
        "entity.villager.work_farmer",
        "entity.villager.work_fisherman",
        "entity.villager.work_fletcher",
        "entity.villager.work_leatherworker",
        "entity.villager.work_librarian",
        "entity.villager.work_mason",
        "entity.villager.work_shepherd",
        "entity.villager.work_toolsmith",
        "entity.villager.work_weaponsmith",
        "entity.villager.yes",
    ],
    "wolf": [
        "entity.wolf.ambient",
        "entity.wolf.death",
        "entity.wolf.growl",
        "entity.wolf.howl",
        "entity.wolf.hurt",
        "entity.wolf.pant",
        "entity.wolf.shake",
        "entity.wolf.step",
        "entity.wolf.whine",
    ],
    "cat": [
        "entity.cat.ambient",
        "entity.cat.beg_for_food",
        "entity.cat.death",
        "entity.cat.eat",
        "entity.cat.hiss",
        "entity.cat.hurt",
        "entity.cat.purr",
        "entity.cat.purreow",
        "entity.cat.stray_ambient",
    ],
    "fall_down": [
        "entity.generic.big_fall",
        "entity.generic.small_fall",
        "entity.hostile.big_fall",
        "entity.hostile.small_fall",
        "entity.player.big_fall",
        "entity.player.small_fall",
    ],
    "firework": ["entity.firework_rocket.launch", "entity.firework_rocket.shoot"],
    "frog": [
        "entity.frog.ambient",
        "entity.frog.death",
        "entity.frog.eat",
        "entity.frog.hurt",
        "entity.frog.lay_spawn",
        "entity.frog.long_jump",
        "entity.frog.step",
        "entity.frog.tongue",
    ],
    "open_chest": ["block.chest.open", "block.ender_chest.open"],
    "pig": [
        "entity.pig.ambient",
        "entity.pig.death",
        "entity.pig.hurt",
        "entity.pig.saddle",
        "entity.pig.step",
    ],
    "raining": ["weather.rain", "weather.rain.above"],
    "warden": [
        "entity.warden.agitated",
        "entity.warden.ambient",
        "entity.warden.angry",
        "entity.warden.attack_impact",
        "entity.warden.death",
        "entity.warden.dig",
        "entity.warden.emerge",
        "entity.warden.heartbeat",
        "entity.warden.hurt",
        "entity.warden.listening",
        "entity.warden.listening_angry",
        "entity.warden.nearby_close",
        "entity.warden.nearby_closer",
        "entity.warden.nearby_closest",
        "entity.warden.roar",
        "entity.warden.sniff",
        "entity.warden.sonic_boom",
        "entity.warden.sonic_charge",
        "entity.warden.step",
        "entity.warden.tendril_clicks",
    ],
    "zombie": [
        "entity.zombie.ambient",
        "entity.zombie.attack_iron_door",
        "entity.zombie.attack_wooden_door",
        "entity.zombie.break_wooden_door",
        "entity.zombie.converted_to_drowned",
        "entity.zombie.death",
        "entity.zombie.destroy_egg",
        "entity.zombie.hurt",
        "entity.zombie.infect",
        "entity.zombie.step",
        "entity.zombie_villager.ambient",
        "entity.zombie_villager.converted",
        "entity.zombie_villager.cure",
        "entity.zombie_villager.death",
        "entity.zombie_villager.hurt",
        "entity.zombie_villager.step",
    ],
}


def trim_silence(
    audio,
    sample_rate: int,
    threshold_db: float = -50.0,
    frame_ms: float = 10.0,
    pre_roll_ms: float = 50.0,
    post_roll_ms: float = 80.0,
) -> tuple[object, float, float]:
    """Trim quiet leading/trailing frames while keeping small natural edge padding."""
    import numpy as np

    mono = audio.mean(axis=1, dtype=np.float32) if audio.ndim == 2 else audio.astype(np.float32)
    frame_length = max(1, round(sample_rate * frame_ms / 1000.0))
    frame_count = (len(mono) + frame_length - 1) // frame_length
    padded = np.pad(mono, (0, frame_count * frame_length - len(mono)))
    frames = padded.reshape(frame_count, frame_length)
    rms = np.sqrt(np.mean(frames * frames, axis=1) + 1e-20)
    active = np.flatnonzero(rms >= 10.0 ** (threshold_db / 20.0))
    if not len(active):
        raise ValueError("No audible content was found")

    start = max(0, active[0] * frame_length - round(sample_rate * pre_roll_ms / 1000.0))
    end = min(
        len(mono),
        (active[-1] + 1) * frame_length + round(sample_rate * post_roll_ms / 1000.0),
    )
    trimmed = mono[start:end]

    peak = float(np.max(np.abs(trimmed)))
    if peak > 0.98:
        trimmed = trimmed * (0.98 / peak)

    return trimmed, start / sample_rate, (len(mono) - end) / sample_rate


def load_subtitles(vanilla_sounds_path: Path | None) -> dict[str, str]:
    if vanilla_sounds_path is None:
        return {}
    with vanilla_sounds_path.open(encoding="utf-8") as file:
        vanilla = json.load(file)
    return {
        event: data["subtitle"]
        for event, data in vanilla.items()
        if isinstance(data, dict) and isinstance(data.get("subtitle"), str)
    }


def build_event_map() -> dict[str, str]:
    event_map: dict[str, str] = {}
    for event in (PROJECT_DIR / "tools/vanilla_1_21_1_block_place_events.txt").read_text().splitlines():
        if event:
            event_map[event] = "place_block"
    for sound_name, events in EVENT_GROUPS.items():
        for event in events:
            if event in event_map:
                raise ValueError(f"Duplicate sound event mapping: {event}")
            event_map[event] = sound_name
    return event_map


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=PROJECT_DIR / "自制Minecraft音效")
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_DIR / f"src/main/resources/assets/{MOD_ID}/sounds",
    )
    parser.add_argument(
        "--vanilla-sounds",
        type=Path,
        help="Optional Minecraft 1.21.1 sounds.json used to preserve vanilla subtitles.",
    )
    parser.add_argument(
        "--sounds-only",
        action="store_true",
        help="Regenerate sounds.json without re-encoding the audio files.",
    )
    args = parser.parse_args()

    if not args.sounds_only:
        import soundfile as sf

        args.output.mkdir(parents=True, exist_ok=True)
        missing = [name for name in AUDIO_FILES if not (args.source / name).is_file()]
        if missing:
            raise FileNotFoundError("Missing source audio: " + ", ".join(missing))

        for source_name, output_name in AUDIO_FILES.items():
            audio, sample_rate = sf.read(args.source / source_name, always_2d=True, dtype="float32")
            before = len(audio) / sample_rate
            trimmed, removed_start, removed_end = trim_silence(audio, sample_rate)
            destination = args.output / f"{output_name}.ogg"
            sf.write(
                destination,
                trimmed,
                sample_rate,
                format="OGG",
                subtype="VORBIS",
                compression_level=0.6,
            )
            print(
                f"{source_name} -> {destination.name}: {before:.3f}s -> "
                f"{len(trimmed) / sample_rate:.3f}s "
                f"(trimmed {removed_start:.3f}s start, {removed_end:.3f}s end)"
            )

    subtitles = load_subtitles(args.vanilla_sounds)
    sounds_json: dict[str, dict[str, object]] = {}
    for event, sound_name in sorted(build_event_map().items()):
        entry: dict[str, object] = {"replace": True}
        if event in subtitles:
            entry["subtitle"] = subtitles[event]
        sound: dict[str, object] = {"name": f"{MOD_ID}:{sound_name}"}
        if event == "entity.generic.explode" or event == "entity.tnt.primed":
            sound.update({"attenuation_distance": 64, "preload": True})
        elif event.startswith("entity.firework_rocket.") and sound_name == "explosion":
            sound.update({"attenuation_distance": 256, "preload": True})
        entry["sounds"] = [sound]
        sounds_json[event] = entry

    sounds_json_path = PROJECT_DIR / "src/main/resources/assets/minecraft/sounds.json"
    sounds_json_path.write_text(
        json.dumps(sounds_json, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {sounds_json_path} with {len(sounds_json)} complete replacements")


if __name__ == "__main__":
    main()
