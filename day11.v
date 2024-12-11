import os

fn apply_rules(stone i64, mut previous_results map[i64][]i64) ([]i64, map[i64][]i64) {
	if stone in previous_results.keys(){
		return previous_results[stone],previous_results
	}
	if stone == 0 {
		return [i64(1)], previous_results
	}
	stone_str := stone.str()
	if stone_str.len % 2 == 0 {
		digits := stone_str.split('').map(it.i64())
		first_half := digits[..digits.len / 2]
		second_half := digits[digits.len / 2..]

		first_stone := first_half.map(it.str()).join('').i64()
		second_stone := second_half.map(it.str()).join('').i64()

		previous_results[stone] = [first_stone, second_stone]
		return [i64(first_stone), i64(second_stone)], previous_results
	}
	previous_results[stone]=[2024*stone]
	return [2024 * i64(stone)], previous_results
}

fn run() {
	data := os.read_file('data/day11.txt') or {
		eprintln('Failed to read file: data/day11.txt')
		return
	}
	stone_line := data.trim_space().split(' ').map(it.i64())

	mut previous_results := map[i64][]i64{}
	for i in 0 .. 100000000{
		if i%10000==0{
			println(i)
		}
		v, updated_results := apply_rules(i, mut previous_results)
		previous_results = updated_results.clone()
	}


	mut current_stone_line := stone_line.clone()

	for i in 0 .. 75 {
		mut new_stone_line := []i64{}
		for stone in current_stone_line {
			v, updated_results := apply_rules(stone, mut previous_results)
			previous_results = updated_results.clone()
			new_stone_line << v
		}
		current_stone_line = new_stone_line.clone()
		println(i)
		println(current_stone_line.len)
		// println(current_stone_line)
	}
}

fn main() {
	run()
}

// 209412